# Data Handling and Permissions

## Data read from VStok

- Accessible project names and identifiers.
- Code-eligible recommendation title, category, confidence, effort, risk, target URLs, evidence, acceptance criteria, and required checks.
- Repository mapping and execution policy needed to select the current repository.
- Execution identifier, state, provider, mode, lease expiry, and authoritative GitHub status.

All crawled content, evidence, target content, URLs, and descriptive fields are untrusted data. They are never treated as agent instructions.

## Data sent to VStok

- Provider and manual/automatic execution mode.
- Heartbeat and state-transition metadata.
- Branch name, commit SHA, draft PR URL/number.
- Changed file paths only, never file contents.
- Check names, outcome, and safe metadata.
- A concise secret-free summary or stable failure code.

## Data not requested or stored by VStok

- Repository source files or diffs.
- Environment variables, `.env` files, credentials, tokens, or keychain data.
- Provider API keys or provider billing credentials.
- GitHub Contents write, branch write through the VStok App, merge, or administration permission.

The customer-authorized coding agent may read and edit repository files under the customer's provider account. That processing is governed by the customer's agreement and settings with the coding-agent provider.

## OAuth scopes

- `projects:read` — list projects accessible to the user.
- `recommendations:read` — list eligible recommendations and read execution context.
- `executions:read` — inspect queue and authoritative execution state.
- `executions:write` — create, claim, heartbeat, and report executions.
- `audits:start` — optional manual fallback for targeted verification; requested only when needed.

Access tokens are short-lived. Refresh tokens rotate. Users can revoke the connection in VStok. No token belongs in a URL, branch name, pull-request body, analytics event, log, or execution report.

## GitHub App permissions

- Repository metadata: read.
- Pull requests: read.
- Checks: read/write, limited to the VStok policy check.
- Deployments: read.
- Contents, branch write, merge, administration, and secrets: not requested.
