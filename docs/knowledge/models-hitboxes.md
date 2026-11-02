# Custom CS2 models: hitboxes, skeletons, materials and attachment debugging

**Status: troubleshooting guidance, not a released model or a validated universal fix.**

## Separate the failure classes

- **Visible model, wrong position:** check transforms, pivot/origin, attachment target, parent entity and bone binding.
- **Model visible, no correct animation:** inspect rig, animation graph, bone names and exported clips; do not assume an AG2 extension makes a compatible animation.
- **Model invisible or purple/missing textures:** inspect material/texture paths and whether assets are compiled and delivered.
- **Visual model differs from collision/hitbox:** check game-side hitbox/hull and the model's rig or gameplay entity setup; changing a mesh does not guarantee matching collision behavior.
- **Works in editor but not server:** separate local content from Workshop and remote client availability.

## Reproducible test

1. Use a simple **original** model with distinct test material.
2. Verify geometry and skeleton in Blender.
3. Check ModelDoc, build warnings and source vs compiled resource references.
4. Verify world-model and first-person viewmodel separately.
5. Test attachment/animation on a clean test map with a **valid floor and spawn point**.
6. Join with a clean client and inspect missing-asset logs.
7. Only after each stage passes, integrate the model into your own plugin or game mode.

## Distribution policy

Do **not** upload exported game characters, commercial model packs or weapon skins you don't own. It's possible to teach the workflow with original placeholder meshes and screenshots.

## Türkçe özet

**Hitbox, model, iskelet ve animasyon aynı şey değildir.** Birini değiştirmek diğerlerini kendiliğinden düzeltmez. Her aşamayı ayrı test et; özel model dosyalarını izinsiz paylaşma.
