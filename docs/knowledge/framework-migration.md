# Migrating CS2 plugins: CounterStrikeSharp ↔ SwiftlyS2

**Status: experience-based architecture checklist; migration requires test-server verification.**

CounterStrikeSharp and SwiftlyS2 are distinct plugin frameworks. A `.dll` written for one is **not automatically compatible** with the other.

## Migration procedure

1. Create a test server and full backups before replacing a working framework.
2. Inventory **features**, not just binary plugin names: commands, permissions, chat, gameplay events, menus, economy, persistence, Workshop content, and admin actions.
3. List each module's dependencies and possible conflicts (shared commands, event handlers, load order, resource paths).
4. Choose a target framework and port modules **source-to-source** using its documented lifecycle and supported APIs. Do not merely rename or copy the DLLs.
5. Keep game-state calls on the supported game thread. Move expensive DB or file work off-thread, but return to the correct thread before mutating game entities.
6. Treat plugin `Load` and `Unload` as a pair: unsubscribe handlers, cancel timers, remove temporary permissions and entities, and release references on hot reload.
7. Migrate persistent data only through explicit, backed-up schema/version changes.
8. Re-test every command and feature after map changes, player disconnect/reconnect, plugin reload, and server restart.

## Lessons from a modular game-mode package review

- Credit and item balances must survive map transitions and restarts.
- Timers should not trigger a second reward/refund after a player leaves.
- Stable player identity and actual current role must be used instead of assuming 'first player with a permission' is the intended recipient.
- Keep database writes batched and away from the main game loop where possible.
- If an old plugin is removed, verify no leftover hooks or assets still affect gameplay.

## Verified upstream references

- [SwiftlyS2 install](https://swiftlys2.net/docs/installation)
- [SwiftlyS2 official plugin template & lifecycle](https://swiftlys2.net/docs/development/getting-started)
- [CounterStrikeSharp documentation](https://docs.cssharp.dev/)

As of the source checked for this guide, SwiftlyS2's official plugin template uses a **.NET 10 SDK**. Check the upstream guide for future changes, and pin dependencies for reproducibility.

## Türkçe özet

**Framework değiştirmek = kodu uyarlamak + veriyi korumak + yeniden test etmek.** CSS DLL'sini SwiftlyS2 klasörüne taşımak göç sayılmaz.
