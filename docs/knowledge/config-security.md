# CS2 plugin configuration and privacy: security lessons

**Status: patterns identified in past code/log reviews; no private configuration published.**

## Do not ship embedded credentials

A compiled plugin can be inspected. If a default configuration generator writes a real DB password or API token that was embedded in the binary, distributing the plugin may reveal those credentials.

**Better approach:** keep secrets outside code and commits; generate an empty example such as `config.example.json` and require the server operator to enter their own credentials. Use narrowly scoped DB permissions.

If credentials were ever exposed, **rotate them**, do not merely remove the string from the latest commit.

## Do not post raw console logs

Logs may contain IP addresses, user identifiers, local directory structure, DB connection strings or tokens. Create a focused, reviewed excerpt or publish only sanitized aggregates. The FRAGLITH log tool reports **counts only** and cannot sanitize original log lines.

## Transaction security

- Avoid double payouts across duplicate timer/leave callbacks.
- Deduct balance atomically, with a database transaction where needed.
- Record unique settlement identifiers and reject duplicate retries.
- Check caller permissions server-side and validate command arguments.
- Encode user text when rendering into markup.

## Dependency and asset supply chain

Review third-party plugin licenses, source trust, compatibility and update history. Do not distribute private or paid code without permission. When using third-party Workshop assets, check rights, version and dependencies.

## What is intentionally omitted

No server IP/hostname, Discord user private messages, Steam IDs, passwords, tokens, API keys, administrator lists, database dumps, decompiled code or private package information is included.
