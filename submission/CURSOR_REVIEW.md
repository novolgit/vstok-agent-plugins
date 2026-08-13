# Cursor Marketplace Review Checklist

## Listing

- Name, description, icon, website, repository, privacy policy, terms, and support URLs match this package.
- Pricing disclosure states that the plugin is free but VStok Growth or Agency and customer-owned agent compute are required.
- Screenshots contain no private email address, OAuth token, customer data, or secrets.

## Manifest and package

- `.cursor-plugin/plugin.json` references only files included in the repository.
- `mcp.json` uses Streamable HTTP at `https://api.vstok.net/api/mcp/v1` and no embedded credential.
- Skill, rules, hooks, and templates are human-readable and narrowly scoped.
- Safety hook fails closed only on a `vstok/*` execution branch and blocks force-push, merge, non-draft PR creation, default-branch push, and denied paths.

## Manual execution

- OAuth consent is explicit and incremental.
- The agent identifies the current mapped repository before changing code.
- The agent creates one execution and one dedicated branch.
- The agent runs repository-native checks and creates only a draft PR.
- VStok receives metadata, not source or diff.

## Automation

- Auto mode is disabled by default and enabled per repository by an owner.
- Queue claim is atomic and lease-backed; heartbeats extend active work.
- Policy limits confidence, effort, risk, categories, paths, concurrency, and quotas.
- Provider or infrastructure failures before `running` do not consume an execution.

## Failure behavior

- Stale evidence, missing target URLs, ambiguous acceptance criteria, incompatible repositories, expired leases, or denied paths stop execution safely.
- The plugin uses stable, secret-free failure reasons.
- No cosmetic change is manufactured when no code change is required.
