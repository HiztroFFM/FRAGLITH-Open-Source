# HUD and loading screens on community CS2 servers

**Status: capability guidance; custom native loading UI has not been validated.**

It's useful to split visual features into three different groups:

1. **Server-driven game data:** announcements, commands, scores, timers, permissions and UI content exposed by supported server-side features.
2. **Custom game assets:** Workshop content, materials, models and effects that require client-accessible resources.
3. **Native game loading/menu UI:** parts of the client engine that a normal server plugin may not be allowed to replace.

A beautiful HTML mockup is **not proof** that CS2 can display it during map loading. Before promising an animated custom loading screen:
- Check actual client/engine UI constraints for the relevant build.
- Validate the user's journey with a clean client, not only a local screenshot.
- Keep UI capabilities distinguished from external web overlays or video demos.
- Avoid implying that a server-side plugin alone can replace any Valve-managed screen.

For HUD prototypes, prefer small components, clear typography and measured performance impact. Test colors, fonts and animations at real gameplay resolutions.

**Open question:** a native CS2 map-loading screen replacement matching a FiveM-style website was **not confirmed**.
