# Pages and agent boundaries
Every wireframe file uses these pages, in this order: the shared pages first, then the working pages.

| Page | What it is for |
| --- | --- |
| Cover | A short, plain-language guide to the file: what it is, one line per page, start links into Prototype and Showroom, and a link back to the project repository. It can double as the file's thumbnail. |
| Showroom | A curated walkthrough of the design for a particular audience, with narrative, annotations and citations. See the [Showroom policy](showroom.md). |
| Prototype | The cleaned-up version of Workshop: finished work that anyone can click through without hitting dead ends or rough edges. It depends only on the Component Library. A stable starting point can live here. |
| Workshop | The work-in-progress prototype: ideally one prototype that covers everything, finished and unfinished. See [working in Workshop](workshop.md). |
| Scratchpad | Divergent options and in-between variations, such as three approaches to one idea side by side. |
| Component Library | The components the other pages use. |

A project can use different page names when it already has them; its `design-files.json` maps them to these roles.

## How the pages work together
- **Scratchpad and Workshop work as a pair.** Work happens in Workshop. When a design question comes up, options go into Scratchpad, labelled A, B, C. The chosen option is folded into Workshop, and the question, options and reasoning are recorded.
- **Promotion copies finished work into Prototype.** Workshop keeps working. Prototype changes only through promotion, a deliberate, checked step that also saves a named version and writes a change note.
- **Showroom is curated.** Promotion flags Showroom screens that show changed work; updating them is a choice.

## Who may change what
These boundaries are provisional and expected to change with experience. Design tools generally cannot enforce them, so agents follow them as rules.

- **Scratchpad:** agents create options freely when asked to explore.
- **Workshop:** agents change it on request.
- **Component Library:** only with an explicit task, because changes ripple to every page.
- **Prototype:** only through promotion, never edited in place.
- **Showroom:** only when working on it at the user's request, never automatically.
- **Cover:** when the file's structure or start links change.

## Naming
Name pages, boards, layers and tokens by their role, not by how they currently look, so a visual change never forces a rename. Board names say the flow or area, the screen, the state and, when it matters, the viewport, for example "Search · Results · Empty · Mobile".
