$ErrorActionPreference = "Stop"

$workspace = "C:\Users\17128\Documents\tx-skill"
$venvPython = Join-Path $workspace ".venv\Scripts\python.exe"

function Find-ProjectRoot {
  $base = "C:\Users\17128\Desktop\skill"
  $candidates = Get-ChildItem -LiteralPath $base -Directory -ErrorAction Stop
  foreach ($candidate in $candidates) {
    if ((Test-Path -LiteralPath (Join-Path $candidate.FullName "db_report")) -and
        (Test-Path -LiteralPath (Join-Path $candidate.FullName "tracingclaw_finance"))) {
      return $candidate.FullName
    }
  }
  throw "Could not find assignment project under $base"
}

$projectRoot = Find-ProjectRoot

Write-Host "== Runtime =="
python --version
node --version
pip --version

Write-Host "`n== Paths =="
$paths = @(
  $projectRoot,
  (Join-Path $projectRoot "db_report\db_report_skill\SKILL.md"),
  (Join-Path $projectRoot "db_report\test-resource\mock_tdsqlb_v22_7_2.log"),
  (Join-Path $projectRoot "tracingclaw_finance\westock-data\scripts\index.js"),
  (Join-Path $projectRoot "tracingclaw_finance\mx-finance-search\scripts\get_data.py"),
  $venvPython
)
foreach ($p in $paths) {
  Write-Host "$p : $(Test-Path -LiteralPath $p)"
}

Write-Host "`n== Python Packages In Venv =="
& $venvPython -c "import openpyxl, matplotlib, numpy, docx, pandas, yaml; print('db_report Python dependencies OK')"

Write-Host "`n== Finance API Key =="
if (-not $env:EM_API_KEY) {
  $env:EM_API_KEY = [Environment]::GetEnvironmentVariable("EM_API_KEY", "User")
}
if ($env:EM_API_KEY) {
  Write-Host "EM_API_KEY is set"
} else {
  Write-Host "EM_API_KEY is missing"
}

Write-Host "`n== westock-data CLI =="
node (Join-Path $projectRoot "tracingclaw_finance\westock-data\scripts\index.js") help | Select-Object -First 5
