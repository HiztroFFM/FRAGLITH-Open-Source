# CS2 Log Triage Tool / Log Tarama Aracı

**Original, standalone Python code. No plugins, API keys or external dependencies.**

This program reads a **local** CS2 server log and prints **only counts by error category**. It does not upload or print log lines, URLs, IPs, names, file paths or credentials.

## Usage

Requires Python 3.10+.

From the repository root:

```bash
python tools/log_triage.py path/to/your/local-console.log
```

Example output (fictional counts, not a real server log):

```json
{
  "format_version": 1,
  "total_lines": 100,
  "categorized_lines": 7,
  "categories": {
    "asset_loading": 4,
    "disk_space": 2,
    "world_position": 1
  },
  "note": "Heuristic counts only. Inspect raw logs locally. Do not publish unreviewed logs."
}
```

Test:

```bash
python -m unittest discover -s tools/tests -v
```

## Important

- Categories are **heuristics**, not verified root-cause diagnoses.
- The tool may miss errors and may classify some lines incorrectly.
- It does **not** sanitize a copy of the original log because it never generates one.
- Do not post your raw logs publicly without manually reviewing secrets, Steam IDs and private information.

**Local tests:** 3 Python unit tests passed in the development environment. This does not mean the tool was tested against every possible CS2 log format.

---

## Türkçe

`python tools/log_triage.py sunucu.log` komutuyla logu **kendi bilgisayarında** tarayabilirsin. Çıktıya yalnızca hata kategorisi sayıları yazılır. Ham log, IP, şifre veya kullanıcı bilgileri basılmaz. Yine de paylaşmadan önce çıktıyı kontrol et.
