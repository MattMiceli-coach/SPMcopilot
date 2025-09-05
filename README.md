# SPMcopilot
AI-powered Strategic Portfolio Management (SPM) Copilot prototype.  Evaluates initiatives for strategic alignment, capacity impact, and funding variance.  Generates executive-ready one-pagers for intake decisions.

# SPMcopilot

**Strategic Portfolio Management (SPM) Copilot Prototype**  
AI-powered assistant that evaluates initiatives for **strategic alignment, capacity impact, and funding variance**, producing **executive-ready one-pagers** for intake decisions.

---

## 🚀 Vision
Most organizations struggle with:
- ❌ Weak alignment of initiatives to strategy & OKRs  
- ❌ Manual, slow intake and funding decisions  
- ❌ Limited visibility into capacity & financial impact  

**SPMcopilot** addresses these pain points by:
- Mapping new initiatives to strategic themes & OKRs  
- Checking against portfolio capacity & funding blocks  
- Generating a decision-ready **one-pager** (Go / Defer / Split)  

This is the **MVP** for a larger platform of SPM AI agents, including quarterly planning, funding reconciliation, and executive dashboards.

---

## 🛠️ Tech Stack
- **Python 3.11+**
- **LangChain** (agent orchestration)
- **OpenAI API** (LLM reasoning)
- **Streamlit** (demo UI)
- **Postgres + pgvector** (future memory store; mocked in MVP)
- **JSON files** for mock data (epics, strategy, capacity, funding)

---

## 📦 Setup

### 1. Clone the repo
```bash
git clone https://github.com/MattMiceli-coach/SPMcopilot.git
cd SPMcopilot
