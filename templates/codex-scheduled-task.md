# VStok scheduled task

Run this task in the repository selected for the VStok project.

> Use the `vstok-agent-execution` skill. Poll `list_execution_queue` with provider `codex`. If there is an execution mapped to this repository, claim exactly one, maintain its lease, implement only its deterministic acceptance criteria, run repository-native checks, and open a draft PR. If the queue is empty or the repository does not match, make no changes. Never merge or push to the default branch.

Recommended schedule: every 30 minutes. VStok policy and quota checks remain authoritative; the task should not retry a failed claim in the same run.
