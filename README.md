# Wireframe Workflows
Reusable agent skills for wireframing with agents: how a design file's pages are organized, how ideas are explored and folded into work in progress, how finished work is promoted into a navigable prototype, and how it is presented. The procedures are tool-agnostic. Mechanics for a particular design tool, such as connecting to it, running its commands or exporting from it, belong to that tool's own skills, for example Agent Hands' `use-penpot` or the Figma MCP.

**Status:** early. Every planned skill is drafted and awaiting review; the [foundations spike](docs/active-spikes/wireframe-workflow-foundations.md) tracks what is left.

The collection has three kinds of material:

- **Policies** are rules that hold whenever anyone, person or agent, works in a wireframe file. An adopting project's instructions tell agents to read them before touching the design file.
- **Skills** are procedures an agent follows when a request calls for them.
- **References** define the formats and contracts the skills rely on.

## Policies
- [Pages and agent boundaries](policies/pages.md): the pages, how they work together, owned pages, who may change what, and naming by role.
- [Working in Workshop](policies/workshop.md): how changes to the work-in-progress prototype are made.
- [Showroom](policies/showroom.md): how the curated walkthrough is kept.
- [Example content](policies/example-content.md): realistic, labelled, made-up content.
- [Board numbering and canvas layout](policies/board-numbering-and-layout.md): unique navigation addresses, descriptive names, short codes and flow arrangement.
- [Scratchpad and Archive](policies/scratchpad-and-archive.md): flexible exploration groups, explicit status, integration and browsable history.

## Skills
| Skill | Used when |
| --- | --- |
| [setup-wireframe-workflows](setup-wireframe-workflows/SKILL.md) | Adopting the collection, linking a project to its design files, or setting up a file's pages |
| [build-wireframes](build-wireframes/SKILL.md) | Everyday design work: the loop through Workshop, Scratchpad and the Component Library |
| [explore-wireframe-options](explore-wireframe-options/SKILL.md) | Showing several options for a design question |
| [map-user-flows](map-user-flows/SKILL.md) | Working out how someone reaches a goal before its screens are built |
| [merge-wireframes](merge-wireframes/SKILL.md) | Combining several people's Workshop work in Staging |
| [promote-wireframes](promote-wireframes/SKILL.md) | Copying settled work into Prototype |
| [audit-wcag](audit-wcag/SKILL.md) | Checking wireframes against the WCAG criteria a design can show |
| [spec-wireframes](spec-wireframes/SKILL.md) | Writing structured specs of Prototype screens for coding agents |
| [check-implementation](check-implementation/SKILL.md) | Comparing a built product with Prototype and its specs |
| [update-wireframe-workflows](update-wireframe-workflows/SKILL.md) | Bringing a project's adoption up to date with the shared collection |

## References
### What the skills need from a design tool
The skills describe what to do; a design tool's own skill describes how. A tool skill supports this collection by explaining how to do each of the following, under these names:

- **List and create pages**, and change their order.
- **Copy a board** from one page to another.
- **Export a board** as an image.
- **Read prototype links** between boards.
- **Read and write design tokens.**
- **Save a named version** of the file.
- **Lock a board**, an optional guard for promoted work.
- **Store file metadata**, optional, so the design file can record a link back to its project repository.

When a tool cannot do one of these, the skill that needs it says so and falls back to asking the user to do that step by hand.

### Linking a project to its design files
Design files live in the cloud, while a project's documents and exports live in its repository. A `design-files.json` manifest at the root of the folder the design work belongs to, usually the repository root, connects the two. Agents and tools read it to find the right file, to know which page plays which role, and to know where local copies belong.

```json
{
  "schema_version": 1,
  "files": [
    {
      "name": "Wireframes",
      "tool": "penpot",
      "url": "https://design.example/workspace?file-id=11111111-2222-3333-4444-555555555555",
      "file_id": "11111111-2222-3333-4444-555555555555",
      "pages": {
        "cover": "Cover",
        "showroom": "Showroom",
        "prototype": "Prototype",
        "workshop": "Workshop",
        "scratchpad": "Scratchpad",
        "component_library": "Component Library"
      },
      "local": {
        "archive": "Wireframes.penpot",
        "exports": "exports/",
        "tokens": "design-tokens/",
        "specs": "specs/",
        "export_manifest": "penpot-export.json"
      }
    }
  ]
}
```

- `files` lists every design file the project uses; most projects have one.
- `name`, `tool`, `url` and `file_id` identify a file. `tool` names the design tool, such as `penpot` or `figma`, and so which tool skill operates it.
- `pages` maps each standard role to the page's actual name in that file, so a project can keep its own names. A file with several designers adds `"staging"`, and maps each owned role to a list instead, for example `"workshop": [{ "page": "Workshop · Sam", "owner": "Sam" }, { "page": "Workshop · Ana", "owner": "Ana" }]`.
- `pages.archive` optionally maps the shared Archive page, placed last and created when there is historical material to hold. It is a single page name, not an owned-page list; original owners are identified within its groups.
- `local` is optional and says where the project keeps copies: a native archive, image exports, design tokens, specs for coding agents and any tool-specific export manifest.

`pages.archive` is the browsable history page in the design tool; `local.archive` is a native file export. They serve different purposes.

Paths are relative to the manifest's folder. The manifest holds no credentials; file and team identifiers are not secrets, and opening a file still requires access in the design tool. In the other direction, the Cover page links back to the repository, and a tool that can store file metadata also records the repository's address in the file itself.

## Adopting
A project adopts this collection as a pinned, root-level `wireframe-workflows/` Git submodule on a project-specific branch, the same way it adopts [Project Workflows](https://github.com/jcklpe/project-workflows). [setup-wireframe-workflows](setup-wireframe-workflows/SKILL.md) walks through adoption, adds the routing that tells agents to read the policies, and sets up the design file.

## Developing this collection
This repository is the project root for its own development. It adopts Project Workflows at `project-workflows/` for its documentation and work process; [AGENTS.md](AGENTS.md) explains how. Clone with submodules:

```sh
git clone --recurse-submodules https://github.com/jcklpe/wireframe-workflows.git
```

In an existing clone, run `git submodule update --init --recursive`. The submodule checks out the exact commit this repository pins, which can leave it on a detached HEAD; select its project branch before editing it.

## License
[AGPL-3.0-only](LICENSE).
