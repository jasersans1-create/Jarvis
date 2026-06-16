from tools.coder import ask_code
import os
import re
import subprocess


WORKSPACE = "generated"


def build_code(prompt):

    os.makedirs(
        WORKSPACE,
        exist_ok=True
    )

    filename = (
        prompt.lower()
        .replace("code", "")
        .replace("build", "")
        .replace("make", "")
        .strip()
    )

    filename = re.sub(
        r"[^a-z0-9]+",
        "_",
        filename
    )

    if not filename:
        filename = "program"

    path = (
        f"{WORKSPACE}/{filename}.py"
    )

    full_prompt = f"""

Write ONLY Python code.

No markdown.

No explanations.

One file.

Request:
{prompt}

"""

    code = ask_code(
        full_prompt
    )

    code = (
        code
        .replace(
            "```python",
            ""
        )
        .replace(
            "```",
            ""
        )
        .strip()
    )

    with open(
        path,
        "w"
    ) as f:

        f.write(
            code
        )

    subprocess.Popen(
        [
            "code",
            path
        ]
    )

    return path