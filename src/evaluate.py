from .tools import get_epic, get_capacity, get_funding, get_strategy_alignment
from .models import Evaluation

def evaluate_epic(epic_id: str) -> Evaluation:
    epic = get_epic(epic_id)
    align = get_strategy_alignment(epic)
    cap = get_capacity(epic.portfolio_id, epic.quarter)
    fund = get_funding(epic.funding_block, epic.quarter)

    headroom = cap.team_capacity_points - cap.committed_points
    post_committed = cap.committed_points + epic.estimate_points
    util_post_pct = round(post_committed / cap.team_capacity_points * 100, 1)

    # simple cost estimate: $2,500 per point
    estimate_usd = epic.estimate_points * 2500
    variance = fund.available_usd - estimate_usd

    # naive recommendation
    if align.score_pct >= 66 and util_post_pct <= 95 and variance >= 0:
        rec = "Go"
        why = "High alignment, capacity within 95%, funding available."
    elif align.score_pct < 33:
        rec = "Defer"
        why = "Weak strategic alignment."
    elif variance < 0:
        rec = "Split"
        why = "Funding shortfall; consider phasing."
    else:
        rec = "Defer"
        why = "Capacity over-commitment or unclear benefit."

    return Evaluation(
        epic_id=epic_id,
        alignment=align,
        capacity_headroom_pts=headroom,
        capacity_utilization_post_pct=util_post_pct,
        funding_variance_usd=variance,
        recommendation=rec,
        rationale=why
    )
