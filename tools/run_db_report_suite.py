from __future__ import annotations

import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path


WORKSPACE = Path(r"C:\Users\17128\Documents\tx-skill")
DESKTOP_SKILL = Path(r"C:\Users\17128\Desktop\skill")
VENV_PYTHON = WORKSPACE / ".venv" / "Scripts" / "python.exe"


def find_project_root() -> Path:
    for candidate in DESKTOP_SKILL.iterdir():
        if candidate.is_dir() and (candidate / "db_report").exists() and (candidate / "tracingclaw_finance").exists():
            return candidate
    raise RuntimeError(f"Could not find assignment project under {DESKTOP_SKILL}")


def run_case(case_id: str, input_text: str, project_root: Path) -> int:
    pipeline = project_root / "db_report" / "db_report_skill" / "scripts" / "run_pipeline.py"
    out_dir = WORKSPACE / "runs" / "db_report" / case_id
    evidence_dir = out_dir / "evidence"

    if out_dir.exists():
        shutil.rmtree(out_dir)
    evidence_dir.mkdir(parents=True, exist_ok=True)
    (evidence_dir / "input.txt").write_text(input_text, encoding="utf-8")

    cmd = [str(VENV_PYTHON), str(pipeline), "--text", input_text, "--out", str(out_dir)]
    proc = subprocess.run(
        cmd,
        cwd=str(project_root),
        text=True,
        encoding="gbk",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    (evidence_dir / "run.log").write_text(proc.stdout, encoding="utf-8")
    (evidence_dir / "exit_code.txt").write_text(str(proc.returncode), encoding="utf-8")

    print(f"=== {case_id} exit={proc.returncode} ===")
    print(proc.stdout[-2000:])
    return proc.returncode


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    project_root = find_project_root()
    records_path = project_root / "db_report" / "test-resource" / "mock_records_aggregation.json"
    records_data = json.loads(records_path.read_text(encoding="utf-8"))
    records = records_data["records"]

    single_rows = [
        row
        for row in records
        if row.get("product") == "TDSQL-B v22.7.3" and row.get("scenario") == "oltp_point_select"
    ][:2]
    large_rows = records[:30]

    single_json = json.dumps(single_rows, ensure_ascii=False, separators=(",", ":"))
    large_json = json.dumps(large_rows, ensure_ascii=False, separators=(",", ":"))

    cases = [
        ("DBR-TC001", "请用 db_report/test-resource/mock_tdsqlb_v22_7_2.log 生成单次数据库性能测试报告。"),
        ("DBR-TC002", "请用 db_report/test-resource/mock_records_aggregation.json 生成性能对比报告。"),
        ("DBR-TC003", f"请基于下面粘贴的 JSON 生成单次性能报告：\n{single_json}"),
        (
            "DBR-TC004",
            "请对比 db_report/test-resource/mock_tdsqlb_v22_7_2.log 和 db_report/test-resource/mock_tdsqlb_v22_7_3.log 的性能差异。",
        ),
        (
            "DBR-TC005",
            "请用 db_report/test-resource/mock_iteration_history.json 生成版本迭代演进报告，回归阈值使用默认 5%。",
        ),
        (
            "DBR-TC006",
            "请基于 db_report/test-resource/mock_records_aggregation.json 生成专项/深度分析报告，重点分析高并发下 P95 稳定性。",
        ),
        ("DBR-TC007", f"请根据下面较大的 records JSON 生成性能报告：\n{large_json}"),
        ("DBR-TC008", "请生成集中式只读场景性能报告。"),
        ("DBR-TC009", "请用 db_report/test-resource/not_exist.log 生成性能测试报告。"),
        (
            "DBR-TC010",
            "请用 db_report/test-resource/mock_tdsqlb_v22_7_3.log 生成报告，并分析 CPU 使用率、锁等待、内存成本和网络瓶颈。",
        ),
    ]

    summary = []
    for case_id, input_text in cases:
        exit_code = run_case(case_id, input_text, project_root)
        summary.append({"case_id": case_id, "exit_code": exit_code})

    summary_path = WORKSPACE / "runs" / "db_report" / "suite_summary.csv"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["case_id", "exit_code"])
        writer.writeheader()
        writer.writerows(summary)

    print(f"Suite summary: {summary_path}")


if __name__ == "__main__":
    main()
