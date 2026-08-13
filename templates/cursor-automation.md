# VStok Cursor Automation template

Create a scheduled Cursor Automation for the selected repository with this instruction:

> Use the `vstok-agent-execution` skill. Poll `list_execution_queue` with provider `cursor`. Claim at most one execution mapped to this repository. Maintain its lease, implement only its deterministic acceptance criteria, run repository-native checks, and open a draft PR. If the queue is empty or mapping does not match, make no changes. Never merge or push to the default branch.

Recommended trigger: every 30 minutes. Enable GitHub access and authenticate the VStok MCP with the repository owner's VStok account. Do not add provider, VStok, or GitHub secrets to the template.
