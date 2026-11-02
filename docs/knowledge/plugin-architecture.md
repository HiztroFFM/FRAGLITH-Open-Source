# Reusable CS2 Plugin Engineering Patterns

**Status: code-reviewed general patterns; not a release of any private game-mode package.** These lessons can be applied to original CounterStrikeSharp or SwiftlyS2 plugins.

## 1. Pay exactly once

A timed result, disconnect callback and plugin unload can all run for the same event. If each handler awards or refunds independently, the total credits can exceed the original stake.

**Pattern:**
- Give each transaction/round a stable unique key.
- Before changing a balance, check its settlement state **atomically**.
- Assign a single terminal outcome (paid, refunded, forfeited or canceled).
- Ignore duplicate settlement callbacks.
- Update balances and transaction state in **one database transaction** where persistence matters.
- Protect against retries after a crash/restart with a unique transaction identifier in the database.

**Important:** A simple in-memory `HashSet` can suppress duplicate callbacks only **until a restart**. For real money-like virtual balances, use a transactional DB ledger.

## 2. Never defer the credit deduction after approval

An input may pass a balance check twice if deduction happens on a later frame. Prevent this with a lock, atomic database update or a serial queue that validates and reserves credits together.

Conceptual SQL for a single account:

```sql
UPDATE accounts
SET balance = balance - :amount
WHERE account_id = :account_id
  AND balance >= :amount;
```

Check affected rows == 1. The rest of a multi-player wager must also be handled transactionally. SQL here is **pseudocode**; parameter binding depends on your driver.

## 3. Persistent counters: write deltas, not every account

For leaderboards and role points:
- Cache legitimate in-memory updates.
- Queue only modified keys to flush in a transaction.
- Rate-limit batch writes.
- Flush on shutdown/map transition where the lifecycle permits.
- Handle failures without silently losing or doubling updates.
- Never block the game loop on full-table DB iteration.

## 4. Get the actual target, not the first admin

If players donate to a current role-holder, resolve the **current active session/role assignment**. The first player with an admin permission is not necessarily that role-holder.

## 5. Escape names in formatted output

If a user-controlled name is concatenated into HTML-like UI markup, it may break layout or mimic formatting. Treat user text as data and encode/sanitize it for the output context.

## 6. Timers, reloads and disconnects

Maintain ownership of scheduled callbacks. On disconnect/round cancellation/reload:
- Cancel or invalidate outstanding timers.
- Release temporary privileges, menus and references.
- Mark the operation terminal before attempting any payout.
- Reconstruct state carefully from persistent data after reload.

## 7. Stay on the appropriate game thread

Do not touch game entity objects from arbitrary DB/background worker threads. Fetch/compute off-thread as permitted, then schedule game-object changes on the framework's supported game-thread path.

## 8. Per-map settings

Spawn points, zones, map bounds and item locations often vary by map. Use distinct configuration sections/files keyed by map identity and validate coordinate ranges before creating entities.

## Tests that should exist

- Duplicate disconnect and timer event produces at most one settlement.
- Two simultaneous transactions cannot overspend a balance.
- Forced plugin reload does not retain transient permissions.
- Map change does not erase persistent balances.
- Missing user input cannot inject formatting.
- Failed DB write can retry without duplicate credit.

**Licensing note:** These are original descriptions of general engineering lessons, not decompiled or redistributed third-party source code.
