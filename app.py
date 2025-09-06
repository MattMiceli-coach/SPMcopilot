from dotenv import load_dotenv
load_dotenv()

import io
import matplotlib.pyplot as plt
import streamlit as st
from src.evaluate import evaluate_epic
from src.tools import get_epic, get_capacity, get_funding
from src.report import to_markdown, to_html

st.title("SPM Copilot — Intake + Alignment + Funding (MVP)")

epic_id = st.selectbox("Choose an Epic", ["EPC-001", "EPC-002"])

if st.button("Run Evaluation"):
    ev = evaluate_epic(epic_id)
    epic = get_epic(epic_id)
    cap = get_capacity(epic.portfolio_id, epic.quarter)
    fund = get_funding(epic.funding_block, epic.quarter)

    st.subheader("Recommendation")
    st.write(f"**{ev.recommendation}** — {ev.rationale}")

    st.subheader("Strategic Alignment")
    st.write(f"Theme: {ev.alignment.theme}")
    st.write(f"OKRs: {', '.join(ev.alignment.okrs) if ev.alignment.okrs else '—'}")
    st.write(f"Score: {ev.alignment.score_pct}%")

    # ---------- Charts ----------
    st.subheader("Capacity")
    # bar: committed vs post-commit vs capacity
    post_committed = cap.committed_points + epic.estimate_points
    fig1, ax1 = plt.subplots()
    ax1.bar(["Committed", "Post-Epic", "Capacity"],
            [cap.committed_points, post_committed, cap.team_capacity_points])
    ax1.set_ylabel("Story Points")
    ax1.set_title("Capacity Utilization")
    st.pyplot(fig1, clear_figure=True)

    st.caption(f"Headroom (pts): {ev.capacity_headroom_pts} • Post Utilization: {ev.capacity_utilization_post_pct}%")

    st.subheader("Funding")
    # bar: available vs est cost (simple $2,500/pt)
    estimate_usd = epic.estimate_points * 2500
    fig2, ax2 = plt.subplots()
    ax2.bar(["Available", "Est. Needed"], [fund.available_usd, estimate_usd])
    ax2.set_ylabel("USD")
    ax2.set_title("Funding Check")
    st.pyplot(fig2, clear_figure=True)

    st.caption(f"Variance (USD): {ev.funding_variance_usd:,}")

    # ---------- Downloads ----------
    md = to_markdown(ev).encode("utf-8")
    st.download_button("Download one-pager (.md)", data=md,
                       file_name=f"{epic_id}_onepager.md", mime="text/markdown")

    html = to_html(ev).encode("utf-8")
    st.download_button("Download one-pager (.html)", data=html,
                       file_name=f"{epic_id}_onepager.html", mime="text/html")

    st.info("Tip: open the .html file in your browser and use **Print → Save as PDF** for a polished PDF.")
