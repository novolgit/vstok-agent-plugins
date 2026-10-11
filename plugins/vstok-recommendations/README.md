# VStok recommendations for Grok Build

Review projects, actionable recommendations, immutable context and execution status. This package does not implement recommendations or start executions in Grok. The server currently supports execution providers Codex, Cursor and Claude.

## Install

Clone https://github.com/novolgit/vstok-agent-plugins and launch `grok --plugin-dir /absolute/path/to/vstok-agent-plugins/plugins/vstok-recommendations`. Open `/mcps` and authenticate the VStok server. Select only projects:read, recommendations:read and executions:read scopes.

The Streamable HTTP endpoint is https://api.vstok.net/api/mcp/v1. OAuth is required and an authorized VStok workspace is needed. No tokens, local executables or hooks are bundled. The MCP server exposes execution tools too; this plugin's workflow uses only the four documented read tools and the user must authorize read scopes only. Do not install the repository root as a Grok execution plugin.

The source is maintained by the product owner under the personal GitHub account novolgit. Plugin configuration is MIT licensed; VStok subscription terms apply separately.

Docs: https://vstok.net/docs/agent-execution
Privacy: https://vstok.net/legal/privacy
Terms: https://vstok.net/legal/terms
Support: https://vstok.net/help

Static package validation does not prove successful OAuth or authenticated runtime behavior in Grok.
