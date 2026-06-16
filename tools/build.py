"""
build.py — AI-powered code generation and file creation.

Generated files are saved to the 'generated/' folder in the project root.
VS Code is launched automatically if available.

Environment variables:
  JARVIS_GENERATED_DIR — directory for generated code (default: ./generated)
"""

import os
import re
import subprocess
import shutil
from pathlib import Path

from tools.coder import ask_code


# Directory where generated code files are saved
_GENERATED_DIR = Path(
    os.getenv("JARVIS_GENERATED_DIR", str(Path(__file__).resolve().parent.parent / "generated"))
)


def build_code(prompt: str) -> str:
    """
    Generate Python code from a natural language prompt and save it to a file.
    Returns the path to the generated file.
    """
    _GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    # Create a safe filename from the prompt
    filename = (
        prompt.lower()
        .replace("code", "")
        .replace("build", "")
        .replace("make", "")
        .replace("create", "")
        .replace("write", "")
        .strip()
    )
    filename = re.sub(r"[^a-z0-9]+", "_", filename).strip("_")

    if not filename:
        filename = "program"

    path = _GENERATED_DIR / f"{filename}.py"

    full_prompt = f"""Write ONLY Python code.

No markdown fences.
No explanations.
One file.
Runnable immediately.

Request: {prompt}
"""

    code = ask_code(full_prompt)

    # Strip any accidental markdown that slipped through
    code = (
        code
        .replace("```python", "")
        .replace("```", "")
        .strip()
    )

    path.write_text(code, encoding="utf-8")
    print(f"[JARVIS] Saved to: {path}")

    # Open in VS Code if available
    if shutil.which("code"):
        subprocess.Popen(["code", str(path)])

    return str(path)