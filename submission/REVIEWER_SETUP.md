# Reviewer Setup

## Accounts supplied privately

VStok will provide marketplace reviewers with these items through the marketplace's secure credential channel, never in this repository:

- A dedicated reviewer email and password for a Growth workspace.
- Access to a VStok project named **VStok Agent Reviewer**.
- Access to the GitHub repository `novolgit/vstok-agent-reviewer-sandbox`.
- Permission to create branches and draft pull requests, but not to bypass branch protection or merge.

The reviewer account must not use an employee's personal account, production customer data, or reusable production credentials.

## Prepared test environment

1. Install the VStok GitHub App on the reviewer sandbox repository.
2. Map the repository to the reviewer project and map the `production` environment.
3. Run a site audit against the sandbox deployment after intentionally removing one approved fixture, such as `FAQPage` JSON-LD.
4. Confirm a fresh `code_safe`, low-risk recommendation exists with a target URL, evidence, deterministic acceptance criteria, and required checks.
5. Keep Codex and Cursor auto mode disabled for manual review.
6. Confirm the reviewer workspace has at least two unused executions.

## Codex review flow

1. Install **VStok Agent Execution**.
2. Approve OAuth scopes `projects:read`, `recommendations:read`, `executions:read`, and `executions:write`.
3. Open the reviewer sandbox repository.
4. Ask: `List code-eligible VStok recommendations for this repository.`
5. Ask: `Implement the best current recommendation to a draft PR.`
6. Confirm the agent creates `vstok/<execution-id>-<slug>`, changes only approved fixture paths, runs `npm test`, and opens a draft PR.
7. Confirm the PR body contains the hidden execution marker and no evidence body, token, or private URL.

## Cursor review flow

Repeat the same flow after installing the Cursor plugin. Verify that the safety hook rejects a force-push, non-draft PR command, default-branch push, or change under a denied path while on a `vstok/*` branch.

## Expected result

The VStok execution timeline moves through agent-reported states only after matching MCP calls. PR and check status becomes authoritative after GitHub webhooks. The recommendation remains incomplete until merge, deployment confirmation, and targeted verification.

## Cleanup

- Close unmerged reviewer PRs.
- Cancel or expire unfinished executions.
- Revoke reviewer OAuth grants.
- Rotate the reviewer password after marketplace review.
- Restore the sandbox fixture and rerun the baseline audit if needed.
