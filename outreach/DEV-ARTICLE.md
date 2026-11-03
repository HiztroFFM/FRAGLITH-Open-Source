---
title: "FRAGLITH: Sharing practical CS2 plugin and Source 2 troubleshooting"
published: false
description: "A free community knowledge base for Counter-Strike 2 plugin developers, Source 2 model porting and AG2 animation debugging."
tags: showdev, gamedev, csharp, beginners
---

# FRAGLITH: Sharing practical CS2 plugin and Source 2 troubleshooting

Developing plugins and custom assets for Counter-Strike 2 often means debugging several layers at once: the plugin framework, game build, compiled assets, Workshop delivery and the actual client.

We started **FRAGLITH • Open Source** as a free space to document what we've learned, invite corrections and make it easier for newcomers to find a useful starting point.

**[Project repository](https://github.com/HiztroFFM/FRAGLITH-Open-Source) | [Discord community](https://discord.gg/Aq8NgGswN)**

## Three things we keep seeing

### 1. A DLL failing to load isn't always a plugin API bug

With CounterStrikeSharp, a message like `Dependency resolution failed` can come from a missing assembly, a deployment folder problem or a framework/runtime mismatch. Checking the actual file layout and the *first* relevant exception is more useful than randomly replacing DLLs.

Our [DLL loading checklist](https://github.com/HiztroFFM/FRAGLITH-Open-Source/blob/main/docs/knowledge/css-plugin-load.md) explains the checks without exposing anybody's private server files.

### 2. Local model previews don't prove the dedicated server can deliver the model

Seeing a model in Workshop Tools validates only part of the process. The next questions are whether the server references the correct compiled content, how a new client receives it and whether viewmodels and worldmodels behave as expected.

We separate each stage in our [Workshop deployment guide](https://github.com/HiztroFFM/FRAGLITH-Open-Source/blob/main/docs/knowledge/workshop-deployment.md).

### 3. Timers, player disconnects and balances need careful state handling

A timed callback and a disconnect event can both attempt to award or refund the same credits. A good plugin needs a single settlement path, safe cancellation, and database-level consistency where persistence matters.

Our [plugin engineering notes](https://github.com/HiztroFFM/FRAGLITH-Open-Source/blob/main/docs/knowledge/plugin-architecture.md) cover this and other lifecycle patterns.

## What is publicly available

- Practical CS2 server/plugin troubleshooting notes
- Source 2, ModelDoc, VData and AG2 workflow checklists
- A [small original Python log-category summary tool](https://github.com/HiztroFFM/FRAGLITH-Open-Source/tree/main/tools) with unit tests
- Contribution guidelines, a public roadmap and newcomer documentation

**What isn't available yet:** a verified complete AG2 port, an animated weapon pack, or production-ready server plugin releases. We label unresolved work clearly instead of pretending it's complete.

## Join us

If you're learning C#, SwiftlyS2, CounterStrikeSharp, Source 2 or model/animation workflows, we'd love corrections, original examples and thoughtful technical discussion.

**GitHub:** https://github.com/HiztroFFM/FRAGLITH-Open-Source

**Discord:** https://discord.gg/Aq8NgGswN

**FRAGLITH — Learn • Build • Share**

---

*For DEV Community: use #showdev and #gamedev, not #opensource for a pure project launch post. This file is a publication draft and has NOT been posted on DEV.to.*
