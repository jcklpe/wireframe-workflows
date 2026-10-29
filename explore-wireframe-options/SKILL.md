---
name: explore-wireframe-options
description: "Lay out several design options side by side in a wireframe file's Scratchpad, help the user choose, fold the choice into Workshop and record the decision. Use for requests such as \"show me three ways to do this\", or when a design question during wireframing has more than one reasonable answer."
---

# Explore Wireframe Options
Answer a design question by showing options instead of guessing. Page rules are in [pages and agent boundaries](../policies/pages.md), and made-up content follows the [example content policy](../policies/example-content.md); the project's `design-files.json` names the file and its pages.

## Scope and authority
Scratchpad, the requester's own when pages have owners, is the one page where the agent may sketch freely. Read Workshop, but change it only once the user has chosen. Leave Prototype, Showroom and the Component Library alone.

## 1. Frame the question
State the question in one sentence, what must stay the same, and how many options to show; default to three unless the user names a number. Read the relevant part of Workshop first, so the options start from what exists.

## 2. Lay out the options
- **One labelled group per question.** Put the question at the top of its group in Scratchpad, then the options side by side, labelled A, B, C, each with a one-line summary of its idea.
- **Make them genuinely different.** Each option should take a different approach, not a small variation of the same one, unless the user asked for variations.
- **Keep the comparison fair.** Use the same viewport, the same content and the same example data in every option, so only the idea differs.
- **Sketch at the right fidelity.** Reuse components and tokens where it is quick, but rough is fine; the point is to compare ideas.

## 3. Present and choose
Export the group as an image and look at it. Describe each option in a sentence or two, with its main trade-off. If you have a recommendation, say so and mark it as yours. Then wait for the user's choice. A mix, such as "B with A's header", is a valid choice.

## 4. Fold the choice into Workshop
Build the chosen option into Workshop following `build-wireframes`: link it into its flow, cover its states and name it by role.

## 5. Record and retire
- **Record the decision** in a short note beside the options: the question, the options, the choice and the user's reasoning in their own words. Specs and later discussions can point to it.
- **Mark the group as decided**, for example "Decided: B", and leave the other options in place as history. Remove them only when the user asks.

Report the question, the choice, what changed in Workshop and where the decision note lives.
