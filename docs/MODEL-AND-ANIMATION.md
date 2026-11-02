# 3D Model & Animation Porting — Starting Checklist

This document is a **workflow checklist**, not a verified one-click porting tutorial. Exact export, compilation, and integration steps vary with CS2 and Workshop Tools versions.

## 1. Check redistribution rights

Use original content or assets covered by a license that permits your intended use. Record creator, source, license, and permitted modifications. Importing a model for personal study does **not** automatically give you permission to redistribute it.

## 2. Prepare the project

- Install [Blender](https://www.blender.org/) and CS2 Workshop Tools.
- Create a clean, versioned workspace for **source** files.
- Keep source files, exported interchange files, and generated game assets separate.

## 3. Validate your asset in Blender

- Inspect object scale, orientation, origin and transforms.
- Check meshes, UV maps, material slots and texture paths.
- For skinned assets, inspect armature structure, bone names, weights, and bind pose.
- For animations, check frame rate, root motion, bone mapping and clip length.
- Export using a supported interchange format, keeping a copy of your original source.

## 4. Process in Source 2 tooling

- Set up your own addon in the Workshop Tools.
- Use appropriate content tools, including ModelDoc for model and animation integration where relevant.
- Validate compile logs and warnings. Fix skeleton or reference mismatches before testing.
- The presence of a compiled animation resource does not prove it will work in every CS2 weapon or viewmodel context.

## 5. Test

- Inspect the model in the supported preview/editor.
- Check world model vs first-person viewmodel behavior separately where applicable.
- Test material visibility, scale, bone transforms, animation transitions and repeated equip/unequip behavior.
- Inspect game/server console logs and keep the exact test versions.
- Test a complete client/server/Workshop installation route if your project depends on server distribution.

## 6. Prepare a useful bug report

```text
CS2 build/version:
OS:
Workshop Tools version (if known):
Blender version:
Model skeleton / animation type:
Export format:
Compile warnings/errors:
Expected result:
Actual result:
Minimal reproducible test asset (redistributable?):
```

## Learn more

- [Source 2 Wiki](https://www.source2.wiki/)
- [Workshop Tools setup](https://www.source2.wiki/Basics/installS2Sdk?game=cs2)
- [Valve Workshop resources](https://www.counter-strike.net/workshop/workshop)

---

# Türkçe özet

Model portlarken **ölçek, kemik/rig, UV-materyal, animasyon ve derleme logları** ayrı ayrı kontrol edilmeli. `.ag2` uzantısını değiştirmek tek başına animasyonu çalıştırmaz. Sadece paylaşma hakkına sahip olduğun dosyaları kullan.
