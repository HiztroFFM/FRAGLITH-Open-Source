# CounterStrikeSharp: DLL / dependency resolution failure

**Status: log-backed diagnosis; not a proven universal fix.**

## Symptom

An example of the *generic* failure class:

```text
Could not load plugin ".../plugins/example/example.dll"
System.InvalidOperationException:
Dependency resolution failed for component ...
Failed to locate managed application ...
```

In an earlier CS2 server log, dependency resolution returned error **-2147450734**. This does **not** by itself prove the plugin API is broken or reveal which file is missing.

## Safe checklist

1. Verify that the expected `.dll` actually exists in the target plugin folder (path spelling and case matter on Linux).
2. Make sure the deployed folder contains **all files produced for that plugin**, not just a copied single DLL if the build uses additional private assemblies.
3. Check compatibility of the plugin build against the currently installed CounterStrikeSharp release and required .NET runtime. Follow that release's install instructions, not an older tutorial.
4. Check whether the loader is looking for the correct target assembly name. Folder name and DLL name can differ.
5. Search surrounding log lines for the **first** dependency resolution, runtime or missing assembly error.
6. Back up and isolate the problem plugin in a test environment; verify it starts before reintroducing other plugins.
7. If the assembly was compiled for another plugin framework, rebuild/port it. A CounterStrikeSharp DLL is not directly a SwiftlyS2 plugin.

## Do not do this

- Don't disable anti-cheat/security features to make arbitrary DLLs load.
- Don't paste your full server directory tree, credentials or private admin config into bug reports.
- Don't assume copying a DLL fixes its dependency graph.

**Outcome:** Analyzing the deployment and .NET environment is the right starting point. The original log did not establish a universal single-command cure.

## Türkçe kısa açıklama

`Dependency resolution failed` hatasında ilk kontrol **dosya yolu, eksik bağımlılık, .NET sürümü ve framework uyumluluğudur**. Başka geliştiricinin DLL'ini izinsiz paylaşmayın.
