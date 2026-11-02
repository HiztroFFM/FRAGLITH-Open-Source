# FRAGLITH — CS2 Development Resources

Curated starting points for plugin development, models, animation and Source 2 tools.

> References are maintained by their respective authors. Their content, versions and compatibility can change. FRAGLITH does not own or endorse third-party code.

## Plugin development

### SwiftlyS2 (C#)

- [SwiftlyS2 documentation](https://swiftlys2.net/docs/) — API, setup, plugin lifecycle and development.
- [SwiftlyS2 getting started](https://swiftlys2.net/docs/development/getting-started/) — official entry point for writing a plugin.
- [SwiftlyS2 source repository](https://github.com/swiftly-solution/swiftlys2) — source and releases.

**Use it for:** developing C# plugins for a supported CS2 server. Check the documentation and the release you actually installed, rather than blindly copying examples across versions.

### CounterStrikeSharp (C#)

- [CounterStrikeSharp documentation](https://docs.cssharp.dev/) — alternative framework for server-side CS2 plugins.
- [CounterStrikeSharp getting started](https://docs.cssharp.dev/docs/guides/getting-started.html) — installation and runtime notes.

**Important:** CounterStrikeSharp and SwiftlyS2 are distinct frameworks with different setup paths and APIs. Do not assume a plugin for one works in the other.

## Source 2 / models / animations

- [Counter-Strike Workshop](https://www.counter-strike.net/workshop/workshop) — Valve's workshop resources and guidance.
- [Source 2 Wiki](https://www.source2.wiki/) — independent, community-maintained documentation for Workshop Tools, ModelDoc and Source 2.
- [Installing CS2 Workshop Tools](https://www.source2.wiki/Basics/installS2Sdk?game=cs2) — community walkthrough for installing the content tools.
- [Blender](https://www.blender.org/) — 3D modelling, rigging and animation.
- [Blender pipeline formats](https://www.blender.org/features/pipeline/) — supported import/export formats and limitations.

### About AG2

AG2 is discussed in the context of Source 2 animation assets and compiled resources. A working pipeline is **not** simply renaming a Blender export to `.ag2`. Model skeletons, compatible animations, compile settings, and validation matter. See our [model and animation starting checklist](MODEL-AND-ANIMATION.md).

## Good first contribution

Please suggest a resource with a clear description, official or original author link, license/permission notes, supported version, and why it's useful. Open an [issue](https://github.com/HiztroFFM/FRAGLITH-Open-Source/issues) or a pull request.

---

# Türkçe

**Eklenti:** SwiftlyS2 veya CounterStrikeSharp'ın kendi belgelerinden başla; API'lerini birbirine karıştırma.

**Model/animasyon:** Önce Blender ile model, UV, materyal, rig ve animasyon verilerini kontrol et. Sonra Source 2/ModelDoc araçlarında derle, CS2'de test et.

**Telif:** İzin almadığın ücretli veya başka bir projeye ait dosyaları burada yayımlama.
