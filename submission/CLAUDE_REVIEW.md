# Claude Directory Review

## Package

- Public repository: <https://github.com/novolgit/vstok-agent-plugins>
- Plugin root: repository root
- Manifest: `.claude-plugin/plugin.json`
- Remote MCP: `.mcp.json`
- Skill: `skills/vstok-agent-execution/SKILL.md`
- Safety hook: `hooks/claude-hooks.json`

## Validation

Run these commands from the repository root:

```bash
claude plugin validate .
claude --plugin-dir .
```

In the test session, open `/mcp`, authorize `vstok`, and run the reviewer flow in `submission/REVIEWER_SETUP.md`.

## Security boundaries

- OAuth uses Dynamic Client Registration, Authorization Code, and PKCE S256.
- Hosted Claude callbacks must use HTTPS; Claude Code may use loopback HTTP.
- The package contains no VStok, GitHub, or Claude secret.
- The agent may only create an isolated branch and draft pull request.
- VStok receives paths and execution metadata, never source files or diffs.
- Crawled evidence is untrusted data and never an instruction source.

## Directory disclosures

The plugin is free to install. A VStok Growth or Agency subscription and customer-owned Claude/GitHub access are required. Anthropic may process recommendation context under the customer's Claude account and direct Anthropic terms. VStok's Privacy Policy, Terms, Subprocessors list, support, and security contact are linked from the public repository and listing copy.
