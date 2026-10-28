# Agent Instructions
This repository owns reusable, tool-agnostic skills for wireframing with agents: file and page structure, the exploration loop, promotion and presentation. Mechanics for a particular design tool belong to that tool's own skills, such as Agent Hands' `use-penpot`; reference them rather than copying them here. A project that adopts this collection keeps its actual design files and documents in its own repository.

## Project workflow
This repository adopts [Project Workflows](project-workflows/README.md) at `project-workflows/`. Read [workflow.toml](project-workflows/workflow.toml) first and resolve its project root relative to that collection. Use its `<skill-name>/SKILL.md` procedures before global workflow seeds; these project instructions override seed defaults. General skills and external-service capabilities remain optional unless the task requires them.

Use [run-project-spike](project-workflows/run-project-spike/SKILL.md) for scoped reasoning and paired task records, [capture-for-later](project-workflows/capture-for-later/SKILL.md) for parked subjects, [setup-project-workflows](project-workflows/setup-project-workflows/SKILL.md) for setup, and [update-project-workflows](project-workflows/update-project-workflows/SKILL.md) for ancestry-aware updates. [TODO.md](TODO.md) indexes active work; paired concepts and tasks live in `docs/active-spikes/`. Create scratch, archive and policy directories only when they have content.

The workflow project branch is `project/wireframe-workflows`, based on shared `main`. Select it before editing the child; verify rather than reset an existing branch. This repository pins the exact child revision. Repository routing does not install skills into clients or prove automatic discovery.

## Writing skills and policies
Rules that must hold whenever anyone works in a design file are policies in `policies/`; procedures that run when a request calls for them are skills. Skills link to the policies rather than restating them.

Skills live directly at the repository root as `<skill-name>/SKILL.md`, named verb-first (for example `build-wireframes`). Keep skills and policies tool-agnostic and plain-language; where a step depends on a design tool, name the capability needed and point to the tool skill that provides it. Name pages, tokens and other semantic structures by their role, not by how they currently look. Examples use synthetic content.

## Git and privacy
Agents may make scoped local commits by explicit pathspec after checking ignores; never force-add, rewrite history unprompted, add co-author trailers, or push. Commit workflow changes in the child first, then record its exact gitlink here. This is a public repository: never commit credentials, private project details or personal machine paths.

## Markdown style
Keep each prose paragraph or comment paragraph on one line and let editors wrap it. Avoid reflow-only edits. Preserve meaningful line breaks and explicit formatter requirements.
