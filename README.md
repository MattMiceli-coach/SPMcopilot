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

## 2. Install dependencies
```bash
pip install -r requirements.txt

3. Add your API key
```bash
Create a .env file with:
OPENAI_API_KEY=your_api_key_here

4. Run the prototype

Run the Python CLI version:
```bash
python main.py

Or launch the Streamlit UI:
```bash
streamlit run app.py

### Part 3 — Workflow & Data
```markdown
## 📊 MVP Workflow
1. Select an **epic** (mock JSON data).  
2. Agent evaluates:  
   - Alignment to strategy & OKRs  
   - Capacity headroom impact  
   - Funding variance impact  
3. Generates an **executive-ready one-pager** with recommendation.  
4. Export as PDF or view in Streamlit UI.  

---

## 🗂️ Data Structure (Mock JSONs)
- **`epics.json`** – sample initiatives (id, title, theme, estimate, funding block, quarter)  
- **`strategy.json`** – strategic themes & OKRs  
- **`capacity.json`** – capacity snapshot by portfolio & quarter  
- **`funding.json`** – funding allocation snapshot

⸻

Part 4 — Roadmap, License, Status

## 📅 Roadmap
### Phase 1 (MVP – Intake Copilot) ✅  
- Mock data + JSON functions  
- Core agent workflow (align → capacity → funding → recommendation)  
- One-pager output  

### Phase 2 – Quarterly Planning Assistant  
- Trade-off slide generation  
- Portfolio-level capacity vs OKRs view  

### Phase 3 – Funding Reconciliation Agent  
- Variance detection  
- Draft change requests  

### Phase 4 – Executive Dashboard Generator  
- Natural language queries → board-ready slides  

---

## ⚖️ License
MIT License (to be confirmed)

---

## ✨ Status
This is a **prototype** intended for demo purposes.  
Not production-ready.  
