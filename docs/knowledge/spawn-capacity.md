# CS2 team capacity / insufficient spawn points

**Status: diagnostic guidance; no third-party plugin code copied.**

Sometimes the server has more player slots than a map provides valid player spawns for one or both teams.

## How to investigate

1. Compare actual player count and game mode/team restrictions with **valid spawn entities** in the map.
2. Check for team-specific spawn limits or spawn collisions.
3. Reproduce with the map and a known number of test players/bots.
4. If adding spawns dynamically, only use **legal, safe coordinates** with appropriate team and map semantics; validate navigation, collision and floor height.
5. Re-check capacity after each map switch and don't leak extra spawn entities across reloads.
6. Track plugin/framework version compatibility.

A publicly available example of the *problem category* is CS2-FullTeamFix. Review its own source and license rather than blindly copying its plugin binary or assuming it runs in another framework.

**Outcome:** A generalized checklist, not a claim that a universal spawn fix was deployed and tested here.
