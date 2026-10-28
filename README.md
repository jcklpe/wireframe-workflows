# Wireframe Workflows
Reusable agent skills for wireframing with agents: how a design file's pages are organized, how ideas are explored and folded into work in progress, how finished work is promoted into a navigable prototype, and how it is presented. The procedures are tool-agnostic. Mechanics for a particular design tool, such as connecting to it, running its commands or exporting from it, belong to that tool's own skills, for example Agent Hands' `use-penpot` or the Figma MCP.

**Status:** early. The first skill, [setup-wireframe-workflows](setup-wireframe-workflows/SKILL.md), is drafted; the rest are planned in the [foundations spike](docs/active-spikes/wireframe-workflow-foundations.md).

## Pages
Every wireframe file uses these pages, in this order: the shared pages first, then the working pages.

| Page | What it is for |
| --- | --- |
| Cover | A short, plain-language guide to the file: what it is, one line per page, and start links into Prototype and Showroom. It can double as the file's thumbnail. |
| Showroom | A guided, linear walkthrough of the design, like a slide deck, with annotations and research citations. |
| Prototype | Finished work that anyone can click through without hitting dead ends. It depends only on the Component Library. A stable starting point can live here. |
| Workshop | Active work in progress, ideally one prototype that covers everything being worked on. |
| Scratchpad | Divergent options and in-between variations, such as three approaches to one idea side by side. |
| Component Library | The components the other pages use. |

A project can use different page names when it already has them; its instructions record the mapping.

## How the pages work together
- **Scratchpad and Workshop work as a pair.** Work happens in Workshop. When a design question comes up, options go into Scratchpad, labelled A, B, C. The chosen option is folded into Workshop, and the question, options and reasoning are recorded.
- **Promotion moves finished work into Prototype.** Prototype changes only through promotion, a deliberate step: move the boards, check that every needed state exists and that nothing dead-ends, refresh Showroom's copies, save a named version, and refresh the project's exports.
- **Showroom stays in step with Prototype.** Showroom holds copies of Prototype screens, refreshed at each promotion and marked with the screen they came from, plus links that open that screen in Prototype.

## Agent boundaries
These are provisional and expected to change with experience. Design tools generally cannot enforce them, so agents follow them as rules.

- Scratchpad: agents create options freely when asked to explore.
- Workshop: agents change it on request.
- Component Library: only with an explicit task, because changes ripple to every page.
- Prototype and Showroom: only through promotion, never edited in place.

## What the skills need from a design tool
The skills describe what to do; a design tool's own skill describes how. A tool skill supports this collection by explaining how to do each of the following, under these names:

- **List and create pages**, and change their order.
- **Copy a board** from one page to another.
- **Export a board** as an image.
- **Read prototype links** between boards.
- **Read and write design tokens.**
- **Save a named version** of the file.
- **Lock a board**, an optional guard for promoted work.

When a tool cannot do one of these, the skill that needs it says so and falls back to asking the user to do that step by hand.

## Adopting
A project adopts this collection as a pinned, root-level `wireframe-workflows/` Git submodule on a project-specific branch, the same way it adopts [Project Workflows](https://github.com/jcklpe/project-workflows). [setup-wireframe-workflows](setup-wireframe-workflows/SKILL.md) walks through adoption and sets up the design file.

## Developing this collection
This repository is the project root for its own development. It adopts Project Workflows at `project-workflows/` for its documentation and work process; [AGENTS.md](AGENTS.md) explains how. Clone with submodules:

```sh
git clone --recurse-submodules https://github.com/jcklpe/wireframe-workflows.git
```

In an existing clone, run `git submodule update --init --recursive`. The submodule checks out the exact commit this repository pins, which can leave it on a detached HEAD; select its project branch before editing it.

## License
[AGPL-3.0-only](LICENSE).
