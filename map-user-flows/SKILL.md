---
name: map-user-flows
description: "Work out the route someone takes through a product to reach a goal, from requirements, research or the existing prototype, and draw it as a flow map in a wireframe file's Scratchpad before its screens are built. Use for requests such as \"work out how someone gets from search to a result\", or when the route through the product is unclear during wireframing."
---

# Map User Flows
Work out how someone gets to a goal before building the screens for it. Page rules are in [pages and agent boundaries](../policies/pages.md); the project's `design-files.json` names the file and its pages, and the tool skill handles the mechanics.

## Scope and authority
Draw only in Scratchpad. Read Workshop, Prototype and the project's requirements and research, but change nothing else. Base the flow on what the user and the sources say; where they are silent, ask rather than invent a need or a step. Research can contain personal details: summarize what it shows, cite where it came from, and never copy personal details into the design file.

## 1. Name the goal
In one sentence, say who the flow is for, by role rather than by an invented persona, what they want to do, where they start and what counts as done, for example "a customer checks when their order will arrive, starting from the confirmation email". Map one goal per flow; a request that covers several goals gets several flows. List the sources the flow draws on: the request, requirements, research, feedback or the existing product.

## 2. Read what exists
When the product already supports part of the goal, read that route first: the Workshop boards and the prototype links between them, and the cleaned-up version in Prototype. The new flow starts from what is there.

## 3. Outline the flow
Write the flow as a short numbered list before drawing anything:

- **Steps:** each screen or moment the person passes through, named by role as its board would be.
- **Actions:** what the person does to move from one step to the next.
- **Branches:** where the route splits, by the person's choice or by what happens, such as no results, an error, a slow load or missing data, and where each branch leads.
- **Ends:** where the person reaches the goal, and where they give up or leave.
- **Sources and open questions:** which source each step rests on, and anything the sources leave unsettled.

Show the outline to the user and settle its open questions before drawing. A question with several reasonable answers can go to [explore-wireframe-options](../explore-wireframe-options/SKILL.md).

## 4. Draw the map
Draw the agreed outline in Scratchpad as one labelled group headed by the goal, for example "Flow: check an order's delivery date".

- **Boxes for steps**, labelled with the screen and state; **arrows for actions**, labelled with what the person does. Each branch gets its own arrow, labelled with its condition.
- **Mark each step** as existing, changed or new, and link existing steps to their Workshop boards.
- **Keep it plain:** boxes, arrows and text, with no screen design.

Export the map as an image and check that it reads clearly.

## 5. Hand off
The new and changed steps are the work list for [build-wireframes](../build-wireframes/SKILL.md), which builds them in Workshop and links them as the map shows. Leave the map in Scratchpad as the reference for that work, and label its status, "Agreed" and later "Built", so later readers know whether it still describes the design.

Report the goal, the sources, the steps and branches, what exists and what is new, any open questions, and where the map is.
