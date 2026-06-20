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

function Invoke-Case {
  param(
    [Parameter(Mandatory=$true)][string]$CaseId,
    [Parameter(Mandatory=$true)][string]$InputText
  )

  $projectRoot = Find-ProjectRoot
  $pipeline = Join-Path $projectRoot "db_report\db_report_skill\scripts\run_pipeline.py"
  $out = Join-Path $workspace "runs\db_report\$CaseId"
  $evidence = Join-Path $out "evidence"
  $log = Join-Path $evidence "run.log"

  if (Test-Path -LiteralPath $out) {
    Remove-Item -LiteralPath $out -Recurse -Force
  }
  New-Item -ItemType Directory -Force -Path $evidence | Out-Null
  Set-Content -LiteralPath (Join-Path $evidence "input.txt") -Value $InputText -Encoding UTF8

  Push-Location $projectRoot
  try {
    Write-Host "=== $CaseId ==="
    & $venvPython $pipeline --text $InputText --out $out 2>&1 | Tee-Object -FilePath $log
    $code = $LASTEXITCODE
  } finally {
    Pop-Location
  }

  Set-Content -LiteralPath (Join-Path $evidence "exit_code.txt") -Value $code -Encoding UTF8
  Write-Host "$CaseId exit code: $code"
}

$projectRoot = Find-ProjectRoot
$recordsPath = Join-Path $projectRoot "db_report\test-resource\mock_records_aggregation.json"
$recordsJson = Get-Content -LiteralPath $recordsPath -Encoding UTF8 -Raw | ConvertFrom-Json
$singleRows = @($recordsJson.records | Where-Object { $_.product -eq "TDSQL-B v22.7.3" -and $_.scenario -eq "oltp_point_select" } | Select-Object -First 2)
$singleJson = ConvertTo-Json $singleRows -Compress -Depth 20
$largeRows = @($recordsJson.records | Select-Object -First 30)
$largeJson = ConvertTo-Json $largeRows -Compress -Depth 20

$cases = @(
  @{
    id = "DBR-TC001"
    text = "请用 db_report/test-resource/mock_tdsqlb_v22_7_2.log 生成单次数据库性能测试报告。"
  },
  @{
    id = "DBR-TC002"
    text = "请用 db_report/test-resource/mock_records_aggregation.json 生成性能对比报告。"
  },
  @{
    id = "DBR-TC003"
    text = "请基于下面粘贴的 JSON 生成单次性能报告：`n$singleJson"
  },
  @{
    id = "DBR-TC004"
    text = "请对比 db_report/test-resource/mock_tdsqlb_v22_7_2.log 和 db_report/test-resource/mock_tdsqlb_v22_7_3.log 的性能差异。"
  },
  @{
    id = "DBR-TC005"
    text = "请用 db_report/test-resource/mock_iteration_history.json 生成版本迭代演进报告，回归阈值使用默认 5%。"
  },
  @{
    id = "DBR-TC006"
    text = "请基于 db_report/test-resource/mock_records_aggregation.json 生成专项/深度分析报告，重点分析高并发下 P95 稳定性。"
  },
  @{
    id = "DBR-TC007"
    text = "请根据下面较大的 records JSON 生成性能报告：`n$largeJson"
  },
  @{
    id = "DBR-TC008"
    text = "请生成集中式只读场景性能报告。"
  },
  @{
    id = "DBR-TC009"
    text = "请用 db_report/test-resource/not_exist.log 生成性能测试报告。"
  },
  @{
    id = "DBR-TC010"
    text = "请用 db_report/test-resource/mock_tdsqlb_v22_7_3.log 生成报告，并分析 CPU 使用率、锁等待、内存成本和网络瓶颈。"
  }
)

$summary = @()
foreach ($case in $cases) {
  Invoke-Case -CaseId $case.id -InputText $case.text
  $exitCode = Get-Content -LiteralPath (Join-Path $workspace "runs\db_report\$($case.id)\evidence\exit_code.txt") -Raw
  $summary += [pscustomobject]@{ case_id = $case.id; exit_code = $exitCode.Trim() }
}

$summaryPath = Join-Path $workspace "runs\db_report\suite_summary.csv"
$summary | Export-Csv -LiteralPath $summaryPath -NoTypeInformation -Encoding UTF8
Write-Host "Suite summary: $summaryPath"

