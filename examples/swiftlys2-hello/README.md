# FRAGLITH Hello — beginner SwiftlyS2 plugin example

**Status: source example, based on current public SwiftlyS2 documentation; not compiled or game-tested in this repository.** Do not treat it as a production-ready release.

This is a small, **new and original** C# plugin example. It logs plugin lifecycle events and replies to the `sw_fraglith` command with the community invitation. It contains no keys, addresses, private data or proprietary model assets.

## Setup

Use the **official plugin template**; do not copy an unrelated framework's DLL.

1. Install the .NET SDK version specified by [SwiftlyS2's current guide](https://swiftlys2.net/docs/development/getting-started) (currently .NET 10).
2. Install the template:

   ```bash
   dotnet new install SwiftlyS2.CS2.PluginTemplate
   dotnet new swplugin -n FraglithHello --PluginName "FRAGLITH Hello" --PluginAuthor "FRAGLITH Contributors"
   ```

3. Replace the generated **main** `FraglithHello.cs` with [this example](FraglithHello.cs).
4. Run `dotnet publish` in the generated project and resolve any SDK/package version differences against upstream docs.
5. Follow SwiftlyS2's documented packaging/install path on a **local test server**.
6. Test the console or in-game `sw_fraglith` command and the plugin's load/unload logs, including hot reload.

## API and version notes

- `[PluginMetadata]`, `BasePlugin` and the lifecycle methods are documented by [SwiftlyS2 Getting Started](https://swiftlys2.net/docs/development/getting-started).
- `[Command]` and `ICommandContext.Reply` are documented by [SwiftlyS2 Commands](https://swiftlys2.net/docs/development/commands).
- These are **public framework interfaces**, not private API endpoints or secrets.
- If a newer SDK changes method names/requirements, open an issue with version and minimal compiler output; please do not share passwords.

## Türkçe

Bu örnek `sw_fraglith` komutuyla Discord bilgisini gösterir ve eklenti yükleme/boşaltma işlemini loglar. **Gerçek CS2 sunucusunda test edildiği iddia edilmiyor.** Önce resmi SwiftlyS2 şablonuyla derleyip test sunucusunda deneyin.
