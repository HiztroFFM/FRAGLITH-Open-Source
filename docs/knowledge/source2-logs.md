# CS2 log triage: asset warnings, load failures and crashes

**Status: based on previous error-log review; each new log requires its own diagnosis.**

A server console may print hundreds of material, model, audio or Workshop lookup warnings without showing a single fatal crash.

## Prioritize the first meaningful failure

| Signal | Possible next check |
| --- | --- |
| `Failed to load`, `not found`, `.vmdl`, `.vpc` | Resource path, compiled output, Workshop package and case sensitivity |
| `Failed to locate managed application` | CounterStrikeSharp plugin DLL/layout/runtime |
| `Failed to preallocate`, `Not enough disk space` | Available update/staging disk capacity |
| `m_vecOrigin`, `outside of cell bounds` | Entity and map/spawn location; note extreme coordinates |
| `Fatal Error`, `Access Violation`, process exit | Investigate crash first and preserve safe reproduction information |
| Animation missing, bone/attachment mismatch | Skeleton, bone markup, graphs, compiled resources |

## A good triage report

- Reproduce one error in a **test environment**.
- Record the relevant framework/game build versions.
- Use a short log excerpt with timestamps around the **first root error**.
- Redact IPs, hostnames, personal names, tokens, full private paths and credentials.
- State expected result versus actual result.
- Mark whether the fix worked only locally, or also on a dedicated server.

## General rules

- A high warning count does not equal a proven crash.
- A generic 'could not load' line often needs the **previous** message to locate the cause.
- Don't claim a particular engine property is broken when logs only show unrelated map positions.
- Restore a known-good backup before experimenting with production servers.

Try our local [log triage helper](../../tools/README.md) for a **first-pass** scan. It is heuristic, not a replacement for manual analysis.
