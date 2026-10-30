# Board numbering and canvas layout
Use this tool-neutral convention when naming and arranging boards within the requested scope. Reorganizing existing design files remains a separate task. Exploration grouping, status and history follow [Scratchpad and Archive](scratchpad-and-archive.md).

## Purpose and terms
Make boards easy to find, distinguish and follow. A board represents a screen, a state of a screen, an overlay, or a partial interface. Use the design tool’s equivalent of a board without making that tool’s terminology or object IDs part of this convention.

A navigation address describes where a screen belongs in the product. A board name describes what this representation shows. A short code abbreviates that name for conversation and references. These identifiers must be unique within their scope; they do not need to persist through a change of purpose, state or hierarchy.

## Navigation addresses
Use dot-separated numbers for the product’s primary navigation hierarchy. For example:

| Address | Screen | Parent |
| --- | --- | --- |
| `1` | Home | — |
| `1.1` | Projects | Home |
| `1.1.1` | Project details | Projects |
| `1.2` | Account | Home |
| `1.2.1` | Sign in | Account |

An address is not a count of clicks or a board’s position in a walkthrough. A journey can visit `1.1.1`, then `1.2.1`, then return to `1.1.1`. Cross-links and returns belong in the flow connections; do not assign a new address for every route into the same screen.

Where navigation is a graph, agree on a primary home for each screen and record the other connections. Do not silently invent a parent to make a graph fit a tree. Numbering describes the product’s navigation, not the design file’s page taxonomy or a particular kind of content hierarchy.

## Board names and scope
Use `Address · Screen name · State`, adding a flow, option, or viewport qualifier when it is needed to distinguish boards. Name the screen by its role and describe meaningful states in plain language.

- `1.1.1 · Project details · Signed out`
- `1.1.1 · Project details · Signed in`
- `1.1.1 · Project details · Signed in · Share flow`

The first two boards share a navigation address but have distinct names. If the same screen and state must appear twice on one design page, distinguish the copies by their actual context rather than leaving ambiguous duplicate names. Reference an existing board when an additional copy serves no purpose.

A full board name and its short code, when used, must each be unique within a design page. Include the file and page when referencing a board outside that scope, for example `Workshop · Sam / 1.1.1.pdso`. Workshop and Prototype may contain corresponding boards with the same local name and code; their page qualification distinguishes them. Resolve collisions when combining work in Staging or moving groups into the shared Archive; retain historical identifiers with their original page and version context.

Viewport is an optional qualifier, not a navigation level. When several viewports are represented, identify them consistently in names and short codes without changing the screen’s hierarchy address.

## Short codes
An optional short code combines the navigation address with a readable abbreviation of the screen name and state:

| Full board name | Short code |
| --- | --- |
| `1.1.1 · Project details · Signed out` | `1.1.1.pdso` |
| `1.1.1 · Project details · Signed in` | `1.1.1.pdsi` |
| `1.1.1 · Project details · Signed in · Share flow` | `1.1.1.pdsi-share` |

Use lowercase letters and, when needed, a readable hyphenated qualifier. Initials are a starting point, not a guarantee of uniqueness. Check the proposed code against the other boards in the page before assigning it. If it collides, expand the abbreviation or add a meaningful qualifier; record the resulting mapping. Do not rely on the collision being unlikely or resolve it silently according to which board an agent finds first.

Keep the full descriptive name available even when a short code is used. A code is shorthand, not a replacement for the explanation of the screen and state. Display it once near the board name when useful; do not create a second title graphic merely to repeat it.

When names, addresses or states change, update the short codes and affected current references together. Separate permanent screen/view IDs are not required. Historical records retain their original identifiers with their version context.

## Overlays and partials
Distinguish navigation destinations from interface pieces displayed within or above them. A board showing a screen with an overlay open keeps the screen’s navigation address and names that state, for example `1.1.1 · Project details · Help open`.

A shared overlay or partial also needs a reference of its own, independent of which screen invokes it. Notation for these references is project-defined and is not another depth in the navigation tree. A project might use `M1 · Help dialog` with short code `M1.help`, but this policy establishes no universal prefix family. Record the project’s chosen notation before using it. A component instance does not need a board address unless it is separately presented as a board.

Show which screens invoke a shared item and what closing or completing it does. Reusing an overlay must preserve the caller’s relevant state and return destination. Do not substitute a convenient existing board if doing so changes unrelated content or exits the current mode.

## Canvas arrangement
Arrange each flow from left to right. Put alternate branches on separate rows, keeping equivalent decision points and shared outcomes aligned where practical. Label the action or condition that leads down each branch and show where it rejoins the flow.

Navigation depth and horizontal progression often coincide, but they need not. Keep addresses meaningful when a flow crosses a branch or returns to a screen; do not renumber boards simply to make their numbers increase across the row. A hierarchy overview and a journey walkthrough may arrange the same screens differently.

Group a flow in a clearly named section or the tool’s equivalent. Leave consistent space for board names, transition labels and connections. Keep related steps close enough to follow, avoid overlapping boards or labels, and route connections so their source and destination are clear. Exact gaps depend on board size and annotation needs; this policy does not prescribe a universal pixel grid.

Keep overlays and partials near the contexts they explain, or in a clearly referenced shared group when several flows use them. Do not imply that an overlay is a full navigation step merely by placing it next in a row. Use explicit labels for opening, closing, returning and changing state.

When comparing viewports, group and label corresponding views without making a viewport change look like the next user action. Showroom may use a curated reading order under its own [policy](showroom.md).

## Titles and supporting information
Use the board or section’s native title where the tool provides one. Do not repeat the same title in a decorative heading, banner or graphic beneath it. An actual heading inside the depicted product interface is different and stays in the wireframe. Exports that omit native titles may include a caption where the title is needed to interpret them.

Keep canvas annotations focused on what a reviewer needs to understand the visible flow: purpose, meaningful state, branch conditions, unresolved choices and relevant source links. Detailed work history and metadata belong in the partner repository.

The repository keeps the current mapping between full names, short codes and design-tool board references, alongside flow relationships, decisions, open questions and export records. Build on the project’s existing manifest and specification formats rather than creating a competing registry. Keep authored decisions distinct from generated observations. Private research may remain in an external source; link it only where its access and privacy boundaries allow.

## Review checks
Before presenting a changed flow, check that:

- Full names and short codes are unique within the stated scope and agree with their mapping.
- Addresses reflect the agreed navigation hierarchy; state, context and viewport qualifiers distinguish the represented boards.
- Branches, cross-links, returns and overlay callers are understandable from the layout and labels.
- Prototype interactions preserve unrelated content and relevant caller state, or explicitly communicate a change to them.
- Names, labels and connectors remain readable without overlaps, clipping or redundant title graphics.
- A renaming or reorganization updates affected current links, mappings and exports without rewriting historical records.
