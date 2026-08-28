import argparse
import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()

parser = argparse.ArgumentParser(description="GitAudit AI: Autonomous Resume & Code Verification Agent")
parser.add_argument("username", type=str, help="Github username of candidate")
parser.add_argument("repo", type=str, help="Github repository name to audit")
parser.add_argument("--resume", type=str, default="data/alana-resume.pdf", help="Path to the candidate's PDF resume")

args = parser.parse_args()

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
    pdf_path = args.resume
    resume_text = extract_pdf_text(pdf_path)

    repo_owner = args.username
    repo_name = args.repo
    
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
    
    At the very end of your response, provide a quantitative score in this exact format:
    **Resume Match Score: [X]%** (calculated based on the proportion of well-supported and partially supported claims versus unsubstantiated ones).
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

    audit_report = response.choices[0].message.content

    print("=== TOOL-ENABLED PDF AUDITING AGENT REPORT ===")
    print(audit_report)

    # Automatically exporting the report to a Markdown (.md) file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"audit_report_{repo_name}_{timestamp}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# GitAudit AI Report - {repo_owner}/{repo_name}\n\n")
        f.write(f"**Generated at:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write(audit_report)

    print(f"\n[+] Report successfully saved to local file: {filename}")

if __name__ == "__main__":
    auditing_agent()