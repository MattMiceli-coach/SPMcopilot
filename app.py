from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from src.evaluate import evaluate_epic

st.title("SPM Copilot — Intake + Alignment + Funding (MVP)")

epic_id = st.selectbox("Choose an Epic", ["EPC-001", "EPC-002"])
if st.button("Run Evaluation"):
    res = evaluate_epic(epic_id)
    st.subheader("Recommendation")
    st.write(f"**{res.recommendation}** — {res.rationale}")

    st.subheader("Strategic Alignment")
    st.write(f"Theme: {res.alignment.theme}")
    st.write(f"OKRs: {', '.join(res.alignment.okrs) if res.alignment.okrs else '—'}")
    st.write(f"Score: {res.alignment.score_pct}%")

    st.subheader("Capacity")
    st.write(f"Post-utilization: {res.capacity_utilization_post_pct}%")
    st.write(f"Headroom (pts): {res.capacity_headroom_pts}")

    st.subheader("Funding")
    st.write(f"Variance (USD): {res.funding_variance_usd:,}")
