from src.evaluate import evaluate_epic

def test_evaluate_runs():
    res = evaluate_epic("EPC-001")
    assert res.recommendation in {"Go", "Defer", "Split"}
