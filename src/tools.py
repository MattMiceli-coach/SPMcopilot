import json
from pathlib import Path
from .models import Epic, Capacity, Funding, AlignmentResult

DATA = Path("data")

def _load_json(name: str):
    with open(DATA / name, "r") as f:
        return json.load(f)

def get_epic(epic_id: str) -> Epic:
    for e in _load_json("epics.json"):
        if e["id"] == epic_id:
            return Epic(**e)
    raise ValueError(f"Epic {epic_id} not found")

def get_capacity(portfolio_id: str, quarter: str) -> Capacity:
    for c in _load_json("capacity.json"):
        if c["portfolio_id"] == portfolio_id and c["quarter"] == quarter:
            return Capacity(**c)
    raise ValueError("Capacity snapshot not found")

def get_funding(block_id: str, quarter: str) -> Funding:
    for f in _load_json("funding.json"):
        if f["block_id"] == block_id and f["quarter"] == quarter:
            return Funding(**f)
    raise ValueError("Funding snapshot not found")

def get_strategy_alignment(epic: Epic) -> AlignmentResult:
    strat = _load_json("strategy.json")
    best_theme, best_hits = None, 0
    for theme in strat["themes"]:
        theme_name = theme["name"]
        keys = [k.lower() for k in strat["keyword_map"].get(theme_name, [])]
        hits = sum(1 for k in epic.keywords if k.lower() in keys)
        if hits > best_hits:
            best_hits = hits
            best_theme = theme
    score = min(100, best_hits * 33)  # crude scoring
    if not best_theme:
        best_theme = {"name": "Unmapped", "okrs": []}
    return AlignmentResult(theme=best_theme["name"], okrs=best_theme["okrs"], score_pct=score)
