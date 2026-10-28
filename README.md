# Wireframe Workflows
Reusable agent skills for wireframing with agents: how a design file's pages are organized, how ideas are explored and folded into work in progress, how finished work is promoted into a navigable prototype, and how it is presented. The procedures are tool-agnostic. Mechanics for a particular design tool, such as connecting to it, running its commands or exporting from it, belong to that tool's own skills, for example Agent Hands' `use-penpot` or the Figma MCP.

**Status:** early. No skills are published yet. The first ones are being designed in the [foundations spike](docs/active-spikes/wireframe-workflow-foundations.md).

## Adopting
Projects will adopt this collection the way they adopt [Project Workflows](https://github.com/jcklpe/project-workflows): as a pinned, root-level Git submodule with a project-specific branch. Adoption instructions will arrive with the first skill.

## Developing this collection
This repository is the project root for its own development. It adopts Project Workflows at `project-workflows/` for its documentation and work process; [AGENTS.md](AGENTS.md) explains how. Clone with submodules:

```sh
git clone --recurse-submodules https://github.com/jcklpe/wireframe-workflows.git
```

In an existing clone, run `git submodule update --init --recursive`. The submodule checks out the exact commit this repository pins, which can leave it on a detached HEAD; select its project branch before editing it.

## License
[AGPL-3.0-only](LICENSE).
