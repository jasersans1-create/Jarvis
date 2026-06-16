from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv("~/Jarvis/.env")

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise RuntimeError("OPENAI_API_KEY not found")

client = OpenAI(
        api_key=key,
        base_url="https://ai.hackclub.com/proxy/v1"
        )

def ask_code(prompt: str) -> str:
        model = "qwen/qwen3-32b"

        print(f"[JARVIS] Using model: {model}")

        response = client.chat.completions.create(
        model=model,
        messages=[
        {
            "role": "system",
            "content": """

You are Jarvis.

Generate ONLY runnable Python.

Rules:

Return ONLY code
Never explain
Never use markdown
Default to one file
Keep code concise
Use beginner friendly Python
Avoid unnecessary libraries

Never generate C/C++/Java
"""
},
{
"role": "user",
"content": prompt
}
]
)

        return response.choices[0].message.content.strip()