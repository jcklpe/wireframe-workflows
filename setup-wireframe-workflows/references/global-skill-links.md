# Optional global discovery
Keep the complete checkout at a stable location: skills reference sibling policies, skills and assets. Linking a skill directory does not install a Figma/Penpot connector, grant file access, or make a project adoption globally authoritative.

Ask which local clients and skills should be linked. The installer supports Codex and Claude Code, needs Python 3.9+ with its standard library, and defaults to a read-only preview. Inspect existing discovery locations first. Defaults are `~/.agents/skills` for Codex and `~/.claude/skills` for Claude Code. Use `--skills-dir` with one client for a verified existing/custom directory, including a Codex installation already using `~/.codex/skills`; do not create duplicate discovery locations. Paths containing symlink directories are refused; select the verified real path explicitly.

From the collection root:
```sh
python3 setup-wireframe-workflows/scripts/link-skills.py --client codex --skill setup-wireframe-workflows --skill build-wireframes
python3 setup-wireframe-workflows/scripts/link-skills.py --client claude --all
```

Repeat `--client` for both clients, or `--skill` for a chosen set. `--all` selects only this collection's root skills; it does not install nested Project Workflows or any service tooling. After reviewing the exact source/destination pairs under the user's authorized selection, repeat the command with `--execute`.

Correct existing links are left unchanged. Files, directories, unrelated links and broken links block the complete selection before writes. There is no overwrite, automatic repair or uninstall. Inspect conflicts with the user rather than deleting their existing skills. An interrupted application can leave some links created; the report lists completed destinations. Preview again to resume safely.

Project instructions take precedence over global discovery. In an adopting project, load its pinned `wireframe-workflows/` and `project-workflows/` directly. Global links are optional convenience for starting elsewhere. Do not replace an existing global link to another checkout simply because a project contains an adoption.

Verify link targets on disk and confirm discovery in a fresh client session. Filesystem checks alone do not establish client discovery. Moving the checkout breaks its links; resolve that deliberately rather than silently repointing them. Other clients can read the files directly; cloud uploads and client-specific packaging are outside this installer.
