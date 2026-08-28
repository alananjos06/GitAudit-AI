import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def extract_pdf_text(pdf_path):
    """Reads the PDF resume file and extracts all text."""
    print(f"Reading PDF resume: {pdf_path}...")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def fetch_github_commits(repo_owner, repo_name):
    """Fetches public commits from a GitHub repository via API."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    print(f"Fetching evidence from GitHub: {repo_owner}/{repo_name}...")
    
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        commit_summary = []
        for commit in commits[:15]:
            author = commit.get("commit", {}).get("author", {}).get("name", "Unknown")
            message = commit.get("commit", {}).get("message", "No message")
            commit_summary.append(f"- Author: {author} | Message: {message}")
        return "\n".join(commit_summary)
    else:
        return f"Could not fetch commits (Error {response.status_code}): please check if the repository is public."

def auditing_agent():
    pdf_path = "data/alana-resume.pdf"
    resume_text = extract_pdf_text(pdf_path)

    repo_owner = "alananjos06"
    repo_name = "educador-financeiro-inteligente"
    
    commit_evidence = fetch_github_commits(repo_owner, repo_name)

    print("\nCross-checking the real PDF resume with GitHub evidence...\n")

    system_prompt = """
    You are a rigorous software engineering and resume auditing agent.
    Your task is to compare the claims found in the candidate's PDF resume with the REAL EVIDENCE obtained from their GitHub commit history.
    Classify the claims as:
    - ✅ Well supported
    - ⚠️ Partially supported
    - ❌ Unsubstantiated / Exaggerated
    Justify your findings strictly based on the provided data. Respond in English.
    """

    user_prompt = f"""
    === PDF RESUME CONTENT ===
    {resume_text}

    === REAL GITHUB EVIDENCE (COMMITS) ===
    {commit_evidence}
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    print("=== TOOL-ENABLED PDF AUDITING AGENT REPORT ===")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    auditing_agent()