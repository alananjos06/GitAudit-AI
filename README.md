# GitAudit AI: Autonomous Resume & Code Verification Agent

> An autonomous agent built to cross-check candidate resume claims against real-world GitHub commit history. Developed for AI hackathons.

## Features

- **PDF Resume Parsing:** Extracts and reads candidate profile text dynamically from PDF files using `pypdf`.
- **GitHub API Integration:** Fetches public commit history and developer activity straight from the GitHub REST API.
- **AI-Powered Cross-Checking:** Leverages Large Language Models to rigorously evaluate resume claims against concrete code evidence.
- **Quantitative Match Score:** Automatically calculates and displays a structured percentage score of candidate profile accuracy.
- **Automated Markdown Reports:** Exports detailed, timestamped audit reports (`.md`) directly to the local environment.
- **Flexible CLI Interface:** Easily run audits for any GitHub username and repository via command-line arguments.

---

## Tech Stack

- **Python 3.10+**
- **OpenAI SDK** (configured with Groq API endpoints)
- **pypdf** (PDF text extraction)
- **Requests** (GitHub REST API communication)
- **Python-dotenv** (Environment security)
- **Argparse** (CLI parsing)

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/alananjos06/GitAudit-AI.git](https://github.com/alananjos06/GitAudit-AI.git)
   cd GitAudit-AI
   ```
### Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate
```

### Install dependencies:
```bash
pip install openai python-dotenv pypdf requests
```

### Configure your environment variables:
Create a .env file in the root directory and add your Groq API key.
```bash
OPENAI_API_KEY=your_groq_api_key_here
```

### How to Run?
Execute the agent via command line by passing the candidate's GitHub username and target repository name:
```bash
python agent_github.py alananjos06 educador-financeiro-inteligente
```
You can also specify a custom resume path using the --resume flag:
```bash
python agent_github.py alananjos06 educador-financeiro-inteligente --resume data/alana-resume.pdf
```

### Output Report
Once executed, the agent prints a detailed analysis classifying claims into:
✅ Well supported
⚠️ Partially supported
❌ Unsubstantiated / Exaggerated
It also outputs a final Resume Match Score and automatically saves a markdown copy (audit_report_<repo>_<timestamp>.md) locally.
