---
name: build-wireframes
description: "Run the everyday wireframing loop: take a request, work it in Workshop, branch into Scratchpad options, the Component Library or flow mapping when the work calls for it, and bring the result back into one connected work-in-progress prototype. Use for everyday requests such as \"add this route to the wireframes\" or \"change how search results look\"."
---

# Build Wireframes
The engine for everyday design work. The rules for each page live in the policies; this skill is the order in which they come into play. Read [pages and agent boundaries](../policies/pages.md), [working in Workshop](../policies/workshop.md), [Scratchpad and Archive](../policies/scratchpad-and-archive.md), and [example content](../policies/example-content.md) first. The project's `design-files.json` names the file and its pages, and the tool skill handles the mechanics.

## The loop
1. **Take the request.** Restate what is being asked in a sentence, and find where it lands in Workshop, the requester's own when pages have owners: which flow, which screens.
2. **Read the current state.** Look at the affected part of Workshop, how it connects, and what the Component Library and tokens offer. Change nothing yet.
3. **Choose the path.**
   - The request is clear: build it in Workshop (step 4).
   - The route through the product is unclear: map it first with [map-user-flows](../map-user-flows/SKILL.md).
   - A design question has one likely answer: ask the user.
   - A design question has several reasonable answers: lay them out with `explore-wireframe-options`, then build the user's choice.
   - The work needs a reusable part the library lacks: draft it locally in Workshop now, and propose the Component Library change as its own task. Once the user approves and the part exists, swap the local draft for the component.
4. **Build in Workshop.** Make the change in small steps, linked into its flow, with its states considered, and with names by role and labelled example content.
5. **Check.** Export the changed boards as images and look at them. Read where each new link leads. For work chosen in Scratchpad, check the affected connected routes before marking the exploration Integrated, link it to the implementation and record verification and remaining work in the repository.
6. **Report and continue.** Say what changed, where it connects, which questions and states are still open, and what was proposed for the Component Library. Then take the next request, or loop back to step 3 for anything left open.

When a flow is finished and the user agrees, hand it to [merge-wireframes](../merge-wireframes/SKILL.md) when the file has Staging, and to [promote-wireframes](../promote-wireframes/SKILL.md) otherwise.
