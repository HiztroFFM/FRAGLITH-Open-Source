# CS2 ModelDoc, AG2 and weapon VData: what we learned

**Status: a mix of editor observations, public schema references and unresolved runtime integration.**

## What was verified locally

- A custom weapon model could be imported and displayed in ModelDoc/Workshop Tools.
- Materials were visible in the test environment.
- This alone **did not prove** animations, first-person weapon attachment, or dedicated-server distribution.
- On inspection, the example asset had no configured animation and no bone markup in the displayed metadata. That is a warning to inspect rig/attachment setup before blaming a server plugin.

## A practical validation order

1. **Authoring:** own/licensed mesh, materials, correct scale/origin, UV and skeleton.
2. **Animation:** identify the source animation, bone hierarchy and retargeting needs. A renamed file is not an AG2 conversion.
3. **ModelDoc/Source 2 compile:** verify animation clips and references compile correctly. Review compiler errors, resource paths and material dependencies.
4. **VData integration:** verify source files and compiled resources are referenced correctly, and check the target game's expected format.
5. **Game test:** separate first-person, world-model and inventory/equip behavior.
6. **Server test:** validate on a test dedicated server with a fresh client and no local authoring files.
7. **Logs:** distinguish out-of-bounds physics/position errors from missing compiled resources and item creation errors.

## Important detail: `m_szWorldModelAg2Override`

Valve's publicly tracked `CBasePlayerWeaponVData` schema includes a field named `m_szWorldModelAg2Override` alongside `m_szWorldModel`.

**Do not conclude that this field is invalid solely because a custom weapon fails.** Existence in a schema, however, does **not** establish that a particular override configuration will work for your asset or game build.

Reference: [GameTracking-CS2 server schema](https://github.com/SteamTracking/GameTracking-CS2/blob/master/DumpSource2/schemas/server/CBasePlayerWeaponVData.h)

## About `m_vecOrigin ... cell bounds`

An example log showed a weapon and HUD model at an extreme negative world Z coordinate, followed by out-of-bounds origin warnings. Check the **map floor, valid spawn and entity positions** first. This log alone does not show that AG2 or a VData property is at fault.

## Known open problems

- End-to-end reliable AG2 port/compile from arbitrary external animation sources
- Stable animated weapon equip/viewmodel behavior in every CS2 runtime context
- Complete remote-client delivery via a dedicated server
- Validated custom weapon creation behavior for every desired VData setup

These require an original reproducible test asset, exact versions and game logs. We do not present a working plugin or animation pack here.

## Türkçe özet

**ModelDoc'ta görünmesi sadece ilk aşama.** Kemikler, animasyon, VData, world/view model, harita koordinatları ve gerçek sunucu dağıtımı tek tek doğrulanmalı.
