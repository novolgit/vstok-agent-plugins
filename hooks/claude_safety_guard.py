#!/usr/bin/env python3
"""Block high-impact operations on an active VStok execution branch."""

from __future__ import annotations

import json
import re
import subprocess
import sys


def current_branch() -> str:
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            check=False,
            capture_output=True,
            text=True,
            timeout=2,
        )
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def deny(reason: str) -> None:
    # Claude Code treats exit 2 from PreToolUse as a blocking decision and
    # presents stderr as the denial reason.
    print(reason, file=sys.stderr)
    raise SystemExit(2)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        deny("VStok safety guard could not validate the tool input.")

    if not current_branch().startswith("vstok/"):
        return

    tool_input = payload.get("tool_input") or {}
    command = str(tool_input.get("command") or "")
    content = str(
        tool_input.get("patch")
        or tool_input.get("input")
        or tool_input.get("content")
        or tool_input.get("file_path")
        or tool_input.get("notebook_path")
        or ""
    )
    candidate = f"{command}\n{content}"

    blocked_commands = (
        (r"\bgit\s+push\b[^\n]*(?:--force|-f\b)", "Force-push is forbidden for VStok executions."),
        (r"\bgit\s+(?:merge|rebase)\b", "Merge and rebase operations are forbidden for VStok executions."),
        (r"\bgh\s+pr\s+merge\b", "VStok executions never merge pull requests."),
        (r"\bgh\s+pr\s+create\b(?![^\n]*--draft)", "VStok pull requests must be created as drafts."),
        (r"\bgit\s+push\b[^\n]*(?:\bmain\b|\bmaster\b)", "Direct pushes to a default branch are forbidden."),
    )
    for pattern, reason in blocked_commands:
        if re.search(pattern, command, flags=re.IGNORECASE):
            deny(reason)

    protected_paths = re.compile(
        r"(?:^|[\s/])(?:\.env(?:\.[^\s/]*)?|\.github/|\.gitlab-ci\.yml|"
        r"(?:deploy|deployment|terraform|pulumi|k8s|kubernetes)/|"
        r"(?:migrations?|supabase/migrations)/|(?:secrets?|credentials?)(?:[./\s]|$))",
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if protected_paths.search(candidate):
        deny(
            "This path is denied by the default VStok automation policy. "
            "Move the execution to manual review or change the owner policy in VStok."
        )


if __name__ == "__main__":
    main()
