# Workshop/model content: local success versus dedicated server

**Status: local asset preview observed; full server distribution was NOT confirmed.**

## Failure pattern

A custom model can open and display in Workshop Tools / ModelDoc but fail to appear correctly when a player joins a dedicated CS2 server.

These are different validation stages:

| Stage | What it proves |
| --- | --- |
| ModelDoc preview | Editor can locate and load the asset in the authoring environment |
| Local workshop test | Local client has the content and can display it |
| Dedicated server | Server can load/access the required references |
| Fresh remote client | The entire content distribution chain works for a player without preinstalled local assets |

## Diagnostic checklist

1. Confirm the **correct Workshop item** (or another supported content distribution route) is available and accessible.
2. Inspect game console logs for missing or invalid `.vmdl`, compiled model, animation and material references.
3. Verify paths, case sensitivity, dependencies, and expected asset packages. Don't publish private or paid asset files to 'fix' a dependency.
4. Check that the plugin gives the correct model class, that the player actually receives the necessary item, and that client/server versions are compatible.
5. Test on a clean client without local development assets installed.
6. Separate first-person viewmodel issues from third-person/worldmodel issues.
7. Compare dedicated server logs with local test results rather than assuming they match.

## Model libraries and ownership

Workflows, logs **after sanitization**, and original examples are welcome. Third-party models, paid animation sets and other copyrighted content require distribution rights.

## Honest outcome

The earlier custom animated-weapon work reached local/Workshop preview stages, but the dedicated server integration remained unresolved. This guide is a **troubleshooting workflow**, not a completed port release.
