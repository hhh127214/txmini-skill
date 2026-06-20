param(
  [Parameter(Mandatory=$true)]
  [string]$Query,

  [switch]$NoSave
)

$ErrorActionPreference = "Stop"

if (-not $env:EM_API_KEY) {
  $env:EM_API_KEY = [Environment]::GetEnvironmentVariable("EM_API_KEY", "User")
}

if (-not $env:EM_API_KEY) {
  throw "EM_API_KEY is missing. Set it first with: `$env:EM_API_KEY='your_real_key'"
}

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
$script = Join-Path $projectRoot "tracingclaw_finance\mx-finance-search\scripts\get_data.py"

if ($NoSave) {
  & $venvPython $script $Query --no-save
} else {
  & $venvPython $script $Query
}
