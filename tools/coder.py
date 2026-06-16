"""
coder.py — Code generation using AI Hack Club API.

The AI Hack Club API is an OpenAI-compatible API available at:
  https://ai.hackclub.com/proxy/v1

No API key is required — the endpoint is open for Hack Club members.
"""

import os
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

# Load .env from project root (works from any working directory)
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_env_path)

# AI Hack Club API — OpenAI-compatible, no API key required.
_api_key = os.getenv("HACKCLUB_AI_API_KEY", "not-needed")
_base_url = os.getenv("HACKCLUB_AI_BASE_URL", "https://ai.hackclub.com/proxy/v1")
_model = os.getenv("JARVIS_CODE_MODEL", "qwen/qwen3-32b")

client = OpenAI(
    api_key=_api_key,
    base_url=_base_url,
)


def ask_code(prompt: str) -> str:
    """Generate Python code for the given prompt using the AI Hack Club API."""

    print(f"[JARVIS] Generating code with model: {_model}")

    system_prompt = """You are a Python code generator.

Rules:
- Return ONLY runnable Python code
- Never include markdown fences (```python or ```)
- Never add explanations or comments unless critical
- Default to a single file
- Write beginner-friendly, readable Python
- Avoid unnecessary third-party libraries
- Never generate C, C++, or Java
"""

    try:
        response = client.chat.completions.create(
            model=_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"[JARVIS] Code generation error: {e}")
        return f"# Error generating code: {e}"