---
name: build-wireframes
description: "Build or change screens and flows in a wireframe file's Workshop page: add a route, extend a flow, add states or revise existing screens, reusing the file's components and tokens and keeping the work-in-progress prototype clickable. Use for everyday wireframing requests such as \"add this route to the wireframes\" or \"change how search results look\"."
---

# Build Wireframes
Do the everyday design work in Workshop. Page purposes and agent boundaries are defined in the [collection README](../README.md); the project's instructions name its design tool, its file and any page names that differ.

## Scope and authority
Work in Workshop only, unless the user names another page. Prototype changes only through promotion, Showroom only through presentation work, and the Component Library only with an explicit task, because every page uses it.

Many design tools apply changes immediately, and collaborators see them live. Work in small steps, describe larger changes before making them, and save a named version before a big batch. Follow the tool skill for the mechanics of each step.

## 1. Understand the request
Read the project's "Wireframes" instructions and the request. Then read the current state of Workshop without changing anything: the screens and flows that already exist, how they connect, and what the Component Library and design tokens offer.

When something about the request is unclear, ask a specific design question rather than guessing. When a question has several reasonable answers, offer to lay them out as options in Scratchpad with `explore-wireframe-options`, then build whichever the user picks.

## 2. Build
- **Reuse before inventing.** Build from Component Library components and the file's design tokens. When a screen needs a reusable part that does not exist, draw it locally in Workshop and propose adding it to the Component Library as a separate task.
- **Keep one connected prototype.** Link each new screen into the flow it belongs to. Every button and link should lead somewhere, or be clearly marked as not designed yet. Do not leave stray boards that nothing links to.
- **Cover the states as you go.** For each screen, consider what it shows when it is empty, loading, in error or successful, plus any state the flow implies. Build the ones in scope and list the rest as open.
- **Name things by role.** Board names say the flow or area, the screen, the state and, when it matters, the viewport, for example "Search · Results · Empty · Mobile". Layer and group names describe what an element is for, not how it looks.
- **Label example content.** Use believable content that is clearly made up, and say so on the board or in its notes. Never use real personal records.

## 3. Check and report
Export the boards you changed as images and look at them. Click-check the new links by reading where each one leads. Then report:

- which screens and states were added or changed;
- where they connect in the flow;
- design questions still open, and states listed but not built;
- any reusable part proposed for the Component Library.

When a flow is finished and the user agrees, it is ready for promotion with `promote-wireframes`.
