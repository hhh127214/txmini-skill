param(
  [Parameter(Mandatory=$true)]
  [string]$CaseId,

  [Parameter(Mandatory=$true)]
  [string]$InputText
)

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
$pipeline = Join-Path $projectRoot "db_report\db_report_skill\scripts\run_pipeline.py"
$out = Join-Path $workspace "runs\db_report\$CaseId"

New-Item -ItemType Directory -Force -Path $out | Out-Null

Push-Location $projectRoot
try {
  & $venvPython $pipeline --text $InputText --out $out
  $code = $LASTEXITCODE
} finally {
  Pop-Location
}

Write-Host "Output: $out"
Write-Host "Pipeline exit code: $code"
exit $code
