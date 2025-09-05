from pydantic import BaseModel
from typing import List

class Epic(BaseModel):
    id: str
    title: str
    summary: str
    estimate_points: int
    funding_block: str
    portfolio_id: str
    quarter: str
    keywords: List[str]

class Capacity(BaseModel):
    portfolio_id: str
    quarter: str
    team_capacity_points: int
    committed_points: int

class Funding(BaseModel):
    block_id: str
    quarter: str
    allocated_usd: int
    available_usd: int

class AlignmentResult(BaseModel):
    theme: str
    okrs: List[str]
    score_pct: int  # 0-100

class Evaluation(BaseModel):
    epic_id: str
    alignment: AlignmentResult
    capacity_headroom_pts: int
    capacity_utilization_post_pct: float
    funding_variance_usd: int
    recommendation: str
    rationale: str
