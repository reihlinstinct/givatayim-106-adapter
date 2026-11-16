"""Validate tracked layout and flag likely private source values."""

import json
import re
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
rules = json.loads((root / "repo-layout.json").read_text())
paths = subprocess.check_output(["git", "ls-files"], cwd=root, text=True).splitlines()
errors = []
for required in rules["required"]:
    if not (root / required).is_file():
        errors.append(f"missing: {required}")
for path in paths:
    allowed = (
        path in rules["root_allowed"]
        if "/" not in path
        else any(
            path.startswith(folder) and Path(path).suffix in extensions
            for folder, extensions in rules["folders"].items()
        )
    )
    if path == ".github/CODEOWNERS":
        allowed = True
    if not allowed:
        errors.append(f"unexpected path: {path}")
    text = (root / path).read_text()
    if re.search(
        r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|phone[msg]{3}-", text
    ):
        errors.append(f"possible private source: {path}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Layout/privacy checks passed: {len(paths)} tracked files")
