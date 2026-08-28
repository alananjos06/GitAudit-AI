import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def evaluate_resume():
    with open("data/curriculo_sintetico.txt", "r", encoding="utf-8") as file:
        resume_text = file.read()

    print("Sending resume for AI evaluation (baseline without tools)...\n")

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a resume evaluator. Analyze the claims in this text and tell me if they seem true and realistic. Answer directly and concisely in English."},
            {"role": "user", "content": resume_text}
        ]
    )

    print("=== AI BASELINE RESPONSE ===")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    evaluate_resume()