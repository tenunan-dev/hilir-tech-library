# Skills

Agent skills in the shared agentskills format (`SKILL.md` with `name` + `description`
frontmatter). **The canonical home is `tenunan-dev/hilir-skills`** (see that repo's
README): the copy here is a synced mirror, not a fork.

- `skills/techlib-mcp/SKILL.md` — mirror of `hilir-skills/skills/techlib-mcp/SKILL.md`.
- `.claude/skills/techlib-mcp` and `.github/skills/techlib-mcp` — relative symlinks to the
  mirror directory, so Claude Code and GitHub Copilot discover it without duplicating
  content inside this repo.

To update the skill: change it in `hilir-skills`, then re-sync here and to
`~/.agents/skills/techlib-mcp/`. Do not edit the mirror in place. The repository stays
assistant-neutral: a skill step that works in only one tool is a documentation bug (see
AGENTS.md).
