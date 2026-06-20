import json
import os
import shutil
import subprocess
from pathlib import Path


WORKSPACE = Path(r"C:\Users\17128\Documents\tx-skill")
RUN_ROOT = WORKSPACE / "runs" / "tracingclaw_finance"
DESKTOP_SKILL_ROOT = Path(r"C:\Users\17128\Desktop\skill")


def find_project_root() -> Path:
    for candidate in DESKTOP_SKILL_ROOT.iterdir():
        if (candidate / "db_report").exists() and (candidate / "tracingclaw_finance").exists():
            return candidate
    raise RuntimeError(f"Could not find assignment project under {DESKTOP_SKILL_ROOT}")


PROJECT_ROOT = find_project_root()
WESTOCK = PROJECT_ROOT / "tracingclaw_finance" / "westock-data" / "scripts" / "index.js"
MX = PROJECT_ROOT / "tracingclaw_finance" / "mx-finance-search" / "scripts" / "get_data.py"
PYTHON = WORKSPACE / ".venv" / "Scripts" / "python.exe"


CASES = [
    {
        "id": "FIN-TC001",
        "question": "腾讯控股 hk00700 2024 财年净利润是多少？请标明财年、币种和口径。",
        "candidate_answer": None,
        "commands": [
            {"name": "westock_finance", "argv": ["node", str(WESTOCK), "finance", "hk00700"]},
        ],
    },
    {
        "id": "FIN-TC002",
        "question": "腾讯控股 hk00700 2024 财年净利润是多少？",
        "candidate_answer": "腾讯控股 2024 财年净利润为 9999 亿元人民币。",
        "commands": [
            {"name": "westock_finance", "argv": ["node", str(WESTOCK), "finance", "hk00700"]},
        ],
    },
    {
        "id": "FIN-TC003",
        "question": "腾讯控股 hk00700 最近一个已收盘交易日的收盘价是多少？",
        "candidate_answer": None,
        "commands": [
            {"name": "westock_quote", "argv": ["node", str(WESTOCK), "quote", "hk00700"]},
            {"name": "westock_kline", "argv": ["node", str(WESTOCK), "kline", "hk00700", "--period", "day", "--limit", "5"]},
        ],
    },
    {
        "id": "FIN-TC004",
        "question": "请核查：腾讯控股 hk00700 在最近一个交易日上涨超过 5%，这个结论是否属实？",
        "candidate_answer": "腾讯控股最近一个交易日上涨超过 5%。",
        "commands": [
            {"name": "westock_quote", "argv": ["node", str(WESTOCK), "quote", "hk00700"]},
            {"name": "westock_kline", "argv": ["node", str(WESTOCK), "kline", "hk00700", "--period", "day", "--limit", "5"]},
        ],
    },
    {
        "id": "FIN-TC005",
        "question": "请核查腾讯控股 hk00700 是否发布过 2024 年年度业绩相关公告。",
        "candidate_answer": "腾讯控股发布过 2024 年年度业绩公告。",
        "commands": [
            {"name": "westock_notice", "argv": ["node", str(WESTOCK), "notice", "list", "hk00700", "--limit", "5"]},
            {"name": "mx_announcement", "argv": [str(PYTHON), str(MX), "腾讯控股 hk00700 2024 年年度业绩 公告", "--no-save"]},
        ],
    },
    {
        "id": "FIN-TC006",
        "question": "请核查一条关于腾讯控股近期业务动态的新闻结论是否有公开资讯支持。",
        "candidate_answer": "腾讯控股近期发布了新的 AI 业务重大进展。",
        "commands": [
            {"name": "mx_news", "argv": [str(PYTHON), str(MX), "腾讯控股 近期 AI 业务 重大进展 新闻", "--no-save"]},
        ],
    },
    {
        "id": "FIN-TC007",
        "question": "请评价下面金融回答真实性。问题：腾讯控股 hk00700 最近一个已收盘交易日收盘价和 2024 财年营收是多少？",
        "candidate_answer": "腾讯控股最近收盘价约 1 港元，2024 财年营收为 1 亿元人民币。",
        "commands": [
            {"name": "westock_quote", "argv": ["node", str(WESTOCK), "quote", "hk00700"]},
            {"name": "westock_finance", "argv": ["node", str(WESTOCK), "finance", "hk00700"]},
        ],
    },
    {
        "id": "FIN-TC008",
        "question": "不存在科技股份有限公司最新股价是多少？",
        "candidate_answer": None,
        "commands": [
            {"name": "westock_search", "argv": ["node", str(WESTOCK), "search", "不存在科技股份有限公司"]},
        ],
    },
    {
        "id": "FIN-TC009",
        "question": "请核查候选回答是否可信。",
        "candidate_answer": "腾讯控股明年利润一定翻倍，因为内部消息已经确认。",
        "commands": [
            {"name": "mx_internal_claim", "argv": [str(PYTHON), str(MX), "腾讯控股 明年利润 翻倍 内部消息 确认", "--no-save"]},
        ],
    },
    {
        "id": "FIN-TC010",
        "question": "腾讯控股 hk00700 2024 财年营收是多少？",
        "candidate_answer": "腾讯控股 2024 财年营收为其 2023 财年营收数据。",
        "commands": [
            {"name": "westock_finance", "argv": ["node", str(WESTOCK), "finance", "hk00700"]},
        ],
    },
]


def run_command(argv: list[str], case_dir: Path, name: str) -> dict:
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    if not env.get("EM_API_KEY"):
        user_key = os.popen(
            'powershell -NoProfile -Command "[Environment]::GetEnvironmentVariable(\'EM_API_KEY\',\'User\')"'
        ).read().strip()
        if user_key:
            env["EM_API_KEY"] = user_key

    proc = subprocess.run(
        argv,
        cwd=str(WORKSPACE),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    safe_argv = ["<python>" if a == str(PYTHON) else a for a in argv]
    result = {
        "name": name,
        "argv": safe_argv,
        "exit_code": proc.returncode,
        "stdout_file": f"{name}.stdout.txt",
        "stderr_file": f"{name}.stderr.txt",
    }
    (case_dir / f"{name}.stdout.txt").write_text(proc.stdout, encoding="utf-8")
    (case_dir / f"{name}.stderr.txt").write_text(proc.stderr, encoding="utf-8")
    return result


def main() -> None:
    if RUN_ROOT.exists():
        shutil.rmtree(RUN_ROOT)
    RUN_ROOT.mkdir(parents=True, exist_ok=True)

    summary = []
    for case in CASES:
        case_id = case["id"]
        case_dir = RUN_ROOT / case_id / "evidence"
        case_dir.mkdir(parents=True, exist_ok=True)
        (case_dir / "input.json").write_text(
            json.dumps(
                {
                    "case_id": case_id,
                    "question": case["question"],
                    "candidate_answer": case["candidate_answer"],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        command_results = []
        for cmd in case["commands"]:
            command_results.append(run_command(cmd["argv"], case_dir, cmd["name"]))

        (case_dir / "commands.json").write_text(
            json.dumps(command_results, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        summary.append(
            {
                "case_id": case_id,
                "command_count": len(command_results),
                "exit_codes": ",".join(str(item["exit_code"]) for item in command_results),
                "all_commands_success": all(item["exit_code"] == 0 for item in command_results),
            }
        )

    lines = ["case_id,command_count,exit_codes,all_commands_success"]
    for row in summary:
        lines.append(
            f"{row['case_id']},{row['command_count']},{row['exit_codes']},{str(row['all_commands_success']).lower()}"
        )
    (RUN_ROOT / "suite_summary.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print((RUN_ROOT / "suite_summary.csv").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
