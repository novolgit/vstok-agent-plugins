# Marketplace Listing Copy

## Shared identity

- Product name: **VStok Agent Execution**
- Developer: **VStok**
- Category: **Developer Tools**
- Website: <https://vstok.net>
- Documentation: <https://vstok.net/docs/agent-execution>
- Support: <https://vstok.net/help>
- Privacy: <https://vstok.net/legal/privacy>
- Terms: <https://vstok.net/legal/terms>
- Repository: <https://github.com/novolgit/vstok-agent-plugins>

## Short description

Implement verified AI visibility recommendations as safe draft pull requests.

## Full description

VStok Agent Execution connects your coding agent to prioritized, code-eligible recommendations from VStok. It reads the recommendation context and deterministic acceptance criteria through OAuth, verifies that the current GitHub repository is mapped to the project, creates an isolated `vstok/*` branch, makes the smallest compatible change, runs repository-native checks, and opens a draft pull request.

The integration is designed for reviewable execution. It never auto-merges, never pushes directly to the default branch, and treats crawled content as untrusted data. VStok does not receive repository source or diffs. GitHub webhooks confirm the pull request and checks; after deployment, VStok verifies the target URLs before completing the recommendation.

Manual execution is available on eligible recommendations. Repository owners may separately enable constrained scheduled automation with confidence, effort, risk, path, concurrency, and quota policies.

## Key benefits

- Turns measured visibility gaps into reviewable code changes.
- Uses concrete target URLs, evidence, acceptance criteria, and required checks.
- Keeps source code and provider credentials in the customer's environment.
- Produces only isolated branches and draft pull requests.
- Verifies the deployed result before marking work complete.

## Requirements

- VStok Growth or Agency plan.
- VStok GitHub App installed on the target repository.
- Repository mapped to a VStok project and production environment.
- Customer-owned Codex or Cursor account and GitHub write access for the agent.

## Pricing disclosure

The marketplace package is free. Use of Agent Execution requires a paid VStok Growth or Agency subscription and is subject to plan execution limits. Coding-agent compute and GitHub usage are billed or governed separately by the customer's providers.

## Data disclosure summary

The plugin sends project selection, recommendation context, target URLs, evidence, acceptance criteria, execution state, and policy metadata between VStok and the agent. Evidence is marked untrusted. Execution reports return only branch name, commit SHA, draft PR URL/number, changed file paths, named check results, and a secret-free summary. VStok does not request or store repository source, diffs, provider API keys, environment variables, or secrets.

## Suggested screenshots

1. `assets/integrations.png` — GitHub mapping, quotas, policies, and OAuth health.
2. `assets/action-center.png` — prioritized Action Center recommendations.
3. `assets/agent-execution-docs.png` — public workflow and product safety boundaries.
4. `assets/recommendation-execution.png` — execution eligibility and safety status.

The fourth screenshot currently demonstrates stale-evidence blocking and should be replaced with a fresh eligible recommendation before final marketplace submission if the reviewer expects an enabled implementation button.
