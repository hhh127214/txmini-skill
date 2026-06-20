# Environment Runbook

## Prepared Paths

Workspace:

```text
C:\Users\17128\Documents\tx-skill
```

Assignment project:

```text
C:\Users\17128\Desktop\skill\性能工程 Skill 评估专项考题
```

Python virtual environment:

```text
C:\Users\17128\Documents\tx-skill\.venv
```

Run outputs:

```text
C:\Users\17128\Documents\tx-skill\runs
```

## Python Environment

The workspace virtual environment has been created and db_report dependencies have been installed:

- openpyxl
- matplotlib
- numpy
- python-docx
- pandas
- pyyaml

Activate it manually if needed:

```powershell
C:\Users\17128\Documents\tx-skill\.venv\Scripts\Activate.ps1
```

Or call Python directly:

```powershell
C:\Users\17128\Documents\tx-skill\.venv\Scripts\python.exe
```

## EM_API_KEY

Do not place the real key in `SKILL.md` or committed files. Set it as an environment variable before running `mx-finance-search`:

```powershell
$env:EM_API_KEY="your_real_key"
```

Permanent user-level setup:

```powershell
[Environment]::SetEnvironmentVariable("EM_API_KEY", "your_real_key", "User")
```

After permanent setup, reopen PowerShell/Codex so the process can see the new variable.

Safe check:

```powershell
if ($env:EM_API_KEY) { "EM_API_KEY is set" } else { "EM_API_KEY is missing" }
```

## Verified So Far

- Python 3.13.13 is available.
- Node v24.10.0 is available.
- `db_report` single-log pipeline ran successfully for `DBR-TC001`.
- `westock-data help` starts successfully.
- `mx-finance-search` starts but stops until `EM_API_KEY` is set.

