# GitAudit AI: Autonomous Resume & Code Verification Agent

> **GitAudit AI** is an autonomous auditing agent designed to bridge the gap between candidate resumes and real-world software engineering data by cross-referencing PDF resumes with live GitHub commit histories using tool-calling.

---

## Overview & Target User:
- **Target User:** Technical recruiters, engineering managers, hiring platforms, and hackathon judges who need to objectively verify technical claims.
- **The Bottleneck:** Resume inflation and unverified technical claims are major bottlenecks in modern recruitment and hackathons. Traditional screening is manual and slow, while standard LLMs are inherently "naive"—treating any text input as absolute truth without verifying underlying code artifacts.
- **The Value:** GitAudit AI introduces objective, evidence-based validation. By programmatically fetching repository commit logs and parsing PDF credentials, it automates the auditing process and flags exaggerations with transparent justifications.

---

## Iteration Changelog:

| Phase / Iteration | What was built / changed | Driving Evidence / Reason |
| :--- | :--- | :--- |
| **Phase 1: Baseline** (`baseline.py`) | Created a naive LLM evaluation script that reads a text resume and assesses claims without external data. | *Observation:* Standard LLMs accept text at face value, proving the need for external ground truth. |
| **Phase 2: Tool Integration** (`agent_github.py`) | Added PDF parsing (`pypdf`) and GitHub REST API integration to fetch real public repository commit logs. | *Decision:* Enable the agent to perform tool-calling/retrieval to ground its evaluations in real code artifacts. |
| **Phase 3: Advanced Auditing Engine** | Refined system prompts and structured the output into a clear markdown table with strict classifications (✅ Well Supported, ⚠️ Partially Supported, ❌ Unsubstantiated/Exaggerated). | *Feedback:* Judges and recruiters require structured, granular, and transparent justifications rather than vague summaries. |

---

## Reproduction Guide (Step-by-Step):
Follow these instructions to set up and run the project from scratch.

### Prerequisites:
- Python 3.10 or higher
- A Groq API Key (get one free at [groq.com](https://groq.com))

### 1. Clone or Download the Repository:
```bash
git clone [https://github.com/alananjos06/git-audit-ai.git](https://github.com/alananjos06/git-audit-ai.git)
cd git-audit-ai
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Create a requirements.txt file (or install directly)
```Bash
pip install openai python-dotenv pypdf requests
```

### 4. Configure Environment Variables
Create a .env file in the root directory and add your Groq API key:
Snippet de código
OPENAI_API_KEY=your_groq_api_key_here

### 5. Add Your PDF Resume
Ensure your candidate PDF resume is placed inside the data/ folder and named accordingly (e.g., data/alana-resume.pdf).

### 6. Run the Baseline (Naive LLM)
```Bash
python baseline.py
```
Expected Output: An unverified, optimistic evaluation based solely on the text.

### 7. Run the Tool-Enabled Auditing Agent
```Bash
python agent_github.py
```
Expected Output: A detailed audit report comparing the PDF resume claims against real-time GitHub commit evidence, complete with structured tables and classifications.

Technical Metrics & Performance:
Execution Time: ~2 to 5 seconds per full audit run.

Cost: ~$0.00 (leveraging high-speed Groq API free tier).

Libraries Used: openai, pypdf, requests, python-dotenv.

Main Failure Mode & Core Opinion:
Main Failure Mode: The agent's accuracy heavily relies on descriptive commit messages. If a developer uses vague commit messages (e.g., "update code" or "fix bug"), the agent cannot accurately map the commit to a specific architectural claim in the resume.
Core Opinion: Autonomous agents in technical recruitment must move beyond conversational validation. True trust in AI requires deterministic tool-calling that bridges human-written claims with immutable version-control artifacts.

License & Ethics:
This project is built for educational, portfolio, and hackathon evaluation purposes. All data processed is public or provided with explicit consent.

---

### The next pass:
1. Save this `README.md` no seu projeto.
2. Crie o arquivo `requirements.txt` com as dependências:
   ```text
   openai
   python-dotenv
   pypdf
   requests