---
attention: live
---
# Wireframe workflow foundations
Define a tool-agnostic way to organize wireframe files and to work in them with agents, then turn it into this collection's first skills. The first real use is the Landlord Mapper design work in [open-austin/Texas-LandlordMapper-design](https://github.com/open-austin/Texas-LandlordMapper-design), whose hosted Penpot file is called Wireframes.

## Positions the user has adopted
- **Plain names over clever ones.** Pages and skills use boring, self-explanatory names; clarity wins over metaphor.
- **Name by role, not appearance.** Pages, tokens and other semantic structures are named for what they do, so a visual change never forces a rename.
- **Vocabulary.** The design system is the existing, immanent system that organizes a product. Component libraries, token exports and similar files are artifacts that document parts of it, not the system itself.
- **Tool-agnostic method, tool-specific mechanics.** This collection describes how to work; connecting to a design tool, calling its API or MCP server and exporting from it belong to tool skills such as Agent Hands' `use-penpot` or the Figma MCP. Each side references the other.

## Page taxonomy
Adopted by the user on 2026-10-27, with agent boundaries still provisional. The maintained version now lives in the [pages policy](../../policies/pages.md).

| Page | Purpose |
| --- | --- |
| Cover | A concise, plain-language guide to the file's pages, with start links, for example into the prototype's view mode. It can double as the file's thumbnail. |
| Showroom | A guided, linear, almost slide-deck walkthrough of the wireframes for stakeholders, with narrative, annotations and research citations. Curated, not generated. |
| Prototype | The cleaned-up version of Workshop: finished-ish work that people can click through freely without dead ends or rough edges. Self-contained apart from its Component Library dependencies. A stable starting point, such as a reproduction of the current product, can live here. |
| Workshop | The work-in-progress prototype: ideally a single all-encompassing prototype, finished and unfinished parts alike. |
| Scratchpad | Intermediate and divergent variation, such as three approaches to one idea side by side. |
| Component Library | The components the other pages use. |

## Working loops
**Scratchpad and Workshop work together** (adopted). The user asks for something in Workshop, for example a new route. When the agent hits a design question, it asks; on request it lays out labelled options (A, B, C) in Scratchpad; the user picks one; the agent integrates the choice into Workshop.

**Promotion is an explicit event that copies** (adopted). Finished work is copied from Workshop into Prototype in deliberate steps rather than through gradual edits to Prototype. Workshop stays the work-in-progress prototype, and Prototype is its cleaned-up version. A promotion checks states and links, copies the boards, saves a named version in the design tool, writes a change note, flags Showroom screens that show changed work, and refreshes and commits the project's repository exports. The point is a Prototype that changes only at known moments, with a restorable design-tool version and a matching Git commit for each change.

**Showroom is curated** (adopted). Showroom presents the design's narrative to stakeholders, so it changes deliberately rather than automatically. Promotion only flags Showroom screens that show changed work; updating them is the user's choice. Screens shown in Showroom are copies marked with the Prototype screen they came from, plus links that open that screen in Prototype's view mode. Making whole screens into components would give a live link, but it clutters the Component Library. Showroom's form is deliberately left open: no walkthrough has been made yet, so real presentations, their audiences and the material they draw on (recorded feedback, notes, collaborator discussions and research) should shape it before anything is fixed.

**Owned pages and Staging** (adopted 2026-10-29). Pages can have owners: when several people design in one file, each can have their own Workshop and Scratchpad while the other pages stay shared, and their finished work is merged into a Staging page before promotion. A file one person works in needs neither. Work is settled, and ready to promote, when it passes promotion's checks and everyone whose work it includes agrees.

**Merging sorts differences before resolving them** (adopted 2026-10-29). Much of a merge involves no conflict, such as two new routes that branch from a screen Prototype already has. Each remaining difference is either already agreed, accidental drift from agents working separately, or a genuine disagreement between the designers. Drift is fixed toward the Component Library, the tokens and recorded decisions with the owner's confirmation. Disagreements belong to the people involved, and the skill does not mediate them: it holds them back, merges everything that does not depend on them, and picks them up once the people have decided. That makes merging a piece-by-piece process rather than one mechanical pass. Shared parts are compared by what they are, not by how they look.

**Tool limits shape the copy steps.** Penpot's Plugin API changes only the page that is open, so it cannot move boards between pages, and its prototype links stay within a page (tested on the hosted server on 2026-10-29; see Agent Hands' `use-penpot`). Agent Hands' `use-penpot` therefore copies boards between pages through Penpot's backend API with the user's access token, so promotion and merging need no paste where a token is configured; without one, a person pastes the boards and the agent relinks and checks them. Agent Hands' `penpot-design-capabilities` spike records the tests. Figma's prototype links are also limited to one page, which suits the same copy-and-relink approach.

## Agent boundaries by page
Provisional; the user expects to adjust these with experience:

- Scratchpad: the agent creates options freely when exploring at the user's request.
- Workshop: changes on request.
- Component Library: only with an explicit task, because changes ripple to every page.
- Prototype: changed only by promotion, never edited in place.
- Showroom: changed only when working on the presentation at the user's request, never automatically.

Design tools generally cannot enforce per-page permissions, so these rules live in the skill an agent reads first. Locking promoted boards can add a light guard.

## What others do
There is no standard page structure. Teams commonly mix pages that track progress (exploration, work in progress, ready for development, archive) with pages by artifact type (components, prototype, handoff). They mark status in page names and fake folders with divider pages. Published examples include [Ataccama's Figma guide](https://flamingo.ataccama.com/blog/how-to-use-figma) (Ready for Dev, Prototype, Archive), [GitLab's handbook](https://handbook.gitlab.com/handbook/marketing/digital-experience/figma) (a ship icon on engineering-ready pages) and [one team's file-structure write-up](https://clipcontent.substack.com/p/how-we-improved-our-project-and-file-structure-in-figma-78bd79cfc97e).

For agents, published guidance prescribes no page layout. It converges on making files readable node by node, with real components, tokens, auto layout and meaningful layer names, and on writing conventions into a skill or rules file the agent reads before touching the canvas ([let's dev](https://letsdev.de/en/blog/mcp-figma-design-to-code-optimize-ai-workflows), [LogRocket](https://blog.logrocket.com/ux-design/design-to-code-with-figma-mcp/), [Abduzeedo on agents writing to Figma](https://abduzeedo.com/node/89190)). This collection is that rules layer.

On merging, Figma's branching flags conflicts layer by layer, merges a branch all or nothing, and recommends short-lived branches scoped to one piece of work, reviewed like a pull request with a description ([Figma's branching guide](https://www.figma.com/best-practices/branching-in-figma/), [help](https://help.figma.com/hc/en-us/articles/360063144053)). It catches overlapping edits, not two designers solving the same problem differently, which is the harder case. Writing on agents and design systems names the drift to expect: invented token names, values that wander within a session, and decisions forgotten between sessions, with fixes that constrain agents to real components and tokens and check their output ([Superdesign](https://superdesign.dev/blog/ai-design-system-drift), a vendor). Teams that let each designer organize files their own way report that nobody could find the final version, which argues for one shared structure even with owned pages ([LogRocket](https://blog.logrocket.com/ux-design/organizing-figma-files-team-collaboration/)). Most of these sources are practitioner writing rather than studies.

## Policies, skills and references
Adopted by the user on 2026-10-28. Rules that must hold whenever anyone works in a design file are policies, because a skill only loads when a request triggers it; an adopting project's instructions tell agents to read the policies before touching the file. Procedures with steps are skills. Formats and contracts are references in the README.

The policies are [pages and agent boundaries](../../policies/pages.md) (the six pages, how they work together, who may change what, and naming by role), [working in Workshop](../../policies/workshop.md), [Showroom](../../policies/showroom.md) and [example content](../../policies/example-content.md). Showroom in particular is curated work whose form should emerge from real walkthroughs, so it is a policy rather than a procedure.

## Skill map
Adopted by the user on 2026-10-27 and revised on 2026-10-28. Skills are named verb-first and link to the policies rather than restating them. People use the wireframes to discuss the design. Implementation is moving to coding agents, so detailed build information goes to them as structured specs rather than annotated spec sheets for human developers.

| Skill | Used when | Role |
| --- | --- | --- |
| `setup-wireframe-workflows` | Starting a design file, or tidying an existing one | Adopts the collection in a project and creates or retrofits the file's pages, Cover and page order. Mirrors `setup-project-workflows`. Every other skill assumes the structure it establishes. |
| `build-wireframes` | "Add this route to the wireframes" | The engine for everyday work: take the request, read the current state, choose the path (build, ask, map the flow, explore options or propose a Component Library part), build in Workshop under the policies, check, report and loop. |
| `explore-wireframe-options` | "Show me three ways to do X" | The Scratchpad loop: labelled options side by side, the chosen one folded into Workshop, the rest clearly retired. Records the question, the options and the user's reasoning for the choice. The only place the agent may make a mess freely. |
| `promote-wireframes` | "This flow is done" | The only skill that changes Prototype: check that every needed state (empty, loading, error, success) exists and that there are no dead ends, copy the boards, save a named version, write a short "what changed" note, flag affected Showroom screens and trigger the repository exports and specs. |
| `merge-wireframes` | "Combine our Workshops" | Merges several people's Workshop work into Staging piece by piece: brings in work that does not overlap or is already agreed, fixes drift with the owners, and holds back disagreements until the people involved settle them. Adopted 2026-10-29. |
| `update-wireframe-workflows` | The collection improves and a project should catch up | Ancestry-aware updates for adopting projects. Mirrors `update-project-workflows`, and is part of the first set so adoption and updates work from the start. |
| `map-user-flows` | "Work out how someone gets from search to a result" | Turns requirements or research into a flow map, usually in Scratchpad, before screens are built. |
| `audit-wcag` | Checking accessibility | Checks what a wireframe can show: text and background contrast from tokens, text and touch-target sizes, heading order, form labels and errors, and marked focus order and alternative text. Each check cites its WCAG criterion and records pass, fail or not applicable. |
| `spec-wireframes` | Prototype screens are ready to build | Writes a structured spec per Prototype screen for coding agents: purpose, route, components and tokens, states, where each interaction leads, copy and data fields, and links to image exports. Specs live in the project's repository beside its exports and refresh on promotion. |
| `check-implementation` | Something has been built from the wireframes | Compares the running product against Prototype and its specs and lists the differences, closing the loop from design to coding agent to verified build. |

**Design-tool capabilities** are a list in the collection README rather than a skill, because no request triggers them on their own. Each tool skill explains how it does each item under the same names, for example in Agent Hands' `use-penpot`. Token sync and applying a design system stay in the tool skills. `setup-wireframe-workflows` records which tool a project uses and checks that its skill covers the list. A machine-readable capability manifest is possible later if that check should be automated.

Component Library changes start inside `build-wireframes` as proposals, and exports are handled by `promote-wireframes` and the tool skills, until a clear need for a separate skill appears.

**Ideas the user has raised, not yet designed** (2026-10-29):

- `report-bug`: a person clicking through the prototype finds a route that leads somewhere unexpected, or a panel or modal that does not open where expected. The skill would capture where they were, what they did and what they expected, then trace the links to the cause.
- `audit-consistency`: routes built early drift from decisions made later. The skill would check screens against recorded decisions and shared patterns and list what has fallen behind.
- A formatting and style policy for frames: how boards are numbered, given that a site is a tree or graph of screens, and how they are laid out on the canvas. The user's notes from earlier Figma work will inform it.
- A copy-and-paste prompt in the README that sets up the collection through `setup-wireframe-workflows`, and a setup path for designers without Git that links the skills where their agent finds them.
- Adoption in team project repositories, with an instruction in each that points agents to `setup-wireframe-workflows`.

## Linking projects to design files
Adopted by the user on 2026-10-27. Design files live in the cloud while project documents and exports live in a repository, so a project-owned `design-files.json` at the root of the folder the design work belongs to connects them. It lists each design file's name, tool, URL and file ID, maps each standard page role to the file's actual page name, and says where local copies such as archives, image exports, tokens and tool-specific export manifests live. Agents and tool skills read it instead of searching for the right file. In the other direction, the Cover links back to the repository, and a tool that can store file metadata records the repository's address in the file. The README defines the format, and `setup-wireframe-workflows` writes and checks it. An existing tool-specific manifest, such as Landlord Mapper's token export manifest, stays as it is and is referenced from `local`.

## Agent proposals not yet decided
- **Version history instead of an Archive page.** A named version at each promotion keeps superseded work restorable without a graveyard page.
- **Page order.** Published pages first (Cover, Showroom, Prototype), then working pages (Workshop, Scratchpad, Component Library).
- **Entry boards.** A small board at the top of each page saying what the page is for, mainly for newcomers and agents.

## Open questions
- Can Figma's API copy a board from one page to another, or does a person paste there too?
- What exactly should the dead-end check verify? Penpot's API reads each shape's interactions, including overlays, so links and reachability can be checked; whether an overlay opens where a person expects is harder.
- Which pages should a project's repository exports come from? The likely answer is Prototype, with Showroom perhaps exported as a document; the project's manifests own that choice.
- How do teammates' agents find the collection's policies, especially for designers who do not use Git?

## Related work
- **First consumer:** Texas-LandlordMapper-design. Its Wireframes file currently has Showroom, Workshop, Scratchpad and Component Library pages; Cover and Prototype are not yet added.
- **Tool mechanics:** Agent Hands' `setup-penpot` (configuration and keys) and `use-penpot` (MCP connector, design-work mechanics and the manifest-driven token export).
- **Workflow process:** this repository's own documentation follows Project Workflows, adopted at `project-workflows/`.
