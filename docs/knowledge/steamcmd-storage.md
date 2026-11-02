# SteamCMD: `app_update 730`, state `0x202`, storage errors

**Status: log-backed when accompanied by an explicit disk-space error.**

## What we saw

A CS2/SteamCMD update reported state `0x202` and a diagnostic similar to:

```text
Failed to preallocate ... (Not enough disk space)
```

The **not enough disk space** message is the decisive clue. The state code alone does not uniquely mean the disk is full.

## Check and fix safely

- Inspect free space on the **actual drive/volume hosting SteamCMD and its download/staging paths**, not only the game folder.
- Account for the size of the installed game **plus temporary update/download files** and possible rollback data.
- Remove only disposable temporary data that you recognize; **do not delete live game files blindly**.
- Expand the volume or choose a drive with adequate free capacity, then rerun the update.
- If enough free space exists, inspect permissions, filesystem quotas, disk health, antivirus locks, and SteamCMD logs for a different root cause.

Example Linux storage checks:

```bash
df -h
du -sh /path/to/steamcmd /path/to/server
```

On Windows, check the volumes used by the server and SteamCMD in File Explorer or Disk Management.

## Result status

Our earlier log explicitly reported insufficient disk capacity during a large preallocation, so storage was the supported diagnosis. There is **no safe hardcoded minimum drive size** for all installations and future updates.
