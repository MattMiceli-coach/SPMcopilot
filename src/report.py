# src/report.py
from datetime import datetime
from .models import Evaluation
from .tools import get_epic

def to_markdown(ev: Evaluation) -> str:
    epic = get_epic(ev.epic_id)
    lines = [
        f"# Intake Decision — {epic.id}: {epic.title}",
        "",
        f"_Generated: {datetime.utcnow().isoformat(timespec='seconds')}Z_",
        "",
        "## Summary",
        f"- **Recommendation:** **{ev.recommendation}** — {ev.rationale}",
        f"- **Strategic Theme:** {ev.alignment.theme}",
        f"- **OKRs:** {', '.join(ev.alignment.okrs) if ev.alignment.okrs else '—'}",
        f"- **Alignment Score:** {ev.alignment.score_pct}%",
        "",
        "## Capacity",
        f"- **Post Utilization:** {ev.capacity_utilization_post_pct}%",
        f"- **Headroom (pts):** {ev.capacity_headroom_pts}",
        "",
        "## Funding",
        f"- **Variance (USD):** {ev.funding_variance_usd:,}",
        "",
        "## Epic Details",
        f"- **Quarter:** {epic.quarter}",
        f"- **Portfolio:** {epic.portfolio_id}",
        f"- **Funding Block:** {epic.funding_block}",
        f"- **Estimate (story points):** {epic.estimate_points}",
        f"- **Summary:** {epic.summary}",
        "",
        "---",
        "_SPM Copilot (MVP)_"
    ]
    return "\n".join(lines)

def to_html(ev: Evaluation) -> str:
    """Simple HTML so the browser can 'Print to PDF' cleanly."""
    md = to_markdown(ev)
    # super-light transform: replace basic markdown markers
    html = (
        md.replace("\n\n", "<br/>")
          .replace("**", "<b>")
          .replace("# Intake Decision", "<h1>Intake Decision")
          .replace("## ", "<h2>")
          .replace("---", "<hr/>")
          .replace("_", "")
    )
    return f"""<!doctype html>
<html><head>
<meta charset="utf-8"/>
<title>SPM Copilot Report</title>
<style>
  body {{ font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Arial,sans-serif; max-width: 900px; margin: 40px auto; line-height: 1.5; }}
  h1 {{ margin-bottom: .2rem; }}
  h2 {{ margin-top: 1.6rem; }}
  b {{ font-weight: 600; }}
  code {{ background: #f6f8fa; padding: 2px 4px; border-radius: 4px; }}
</style>
</head><body>{html}</body></html>"""
