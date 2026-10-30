---
name: explore-wireframe-options
description: "Lay out several design options side by side in a wireframe file's Scratchpad, help the user choose, fold the choice into Workshop and record the decision. Use for requests such as \"show me three ways to do this\", or when a design question during wireframing has more than one reasonable answer."
---

# Explore Wireframe Options
Answer a design question by showing options instead of guessing. Read [Scratchpad and Archive](../policies/scratchpad-and-archive.md) for grouping, status, integration and history. Page rules are in [pages and agent boundaries](../policies/pages.md), and made-up content follows the [example content policy](../policies/example-content.md); the project's `design-files.json` names the file and its pages.

## Scope and authority
Scratchpad, the requester's own when pages have owners, is the one page where the agent may sketch freely. Read Workshop, but change it only once the user has chosen and integration is within the requested scope. This procedure compares alternatives; loose sketches or studies can follow the Scratchpad policy without being forced into a question-and-choice exercise. Leave Prototype, Showroom and the Component Library alone.

## 1. Frame the question
State the question in one sentence, what must stay the same, and how many options to show; default to three unless the user names a number. Read the relevant part of Workshop first, so the options start from what exists.

## 2. Lay out the options
- **Group the comparison.** Use the question as the native group title, with options labelled A, B, C and a brief difference for each. Apply the policy’s Open status. Keep each option’s sequence distinct from the other alternatives; do not duplicate the group title as a decorative banner.
- **Make them genuinely different.** Each option should take a different approach, not a small variation of the same one, unless the user asked for variations.
- **Keep the comparison fair.** Use comparable viewport, content and example data where practical; identify intentional differences needed to demonstrate an approach.
- **Sketch at the right fidelity.** Reuse components and tokens where it is quick, but rough is fine; the point is to compare ideas.

## 3. Present and choose
Export the group as an image and look at it. Describe each option in a sentence or two, with its main trade-off. If you have a recommendation, say so and mark it as yours. Then wait for the user's choice. A mix, such as "B with A's header", is a valid choice.

## 4. Fold the choice into Workshop
Mark the group Chosen — awaiting integration and identify the selected option. Build it into Workshop following [build-wireframes](../build-wireframes/SKILL.md) within the authorized scope. Check affected routes, states, entry points and exits. Only then mark the group Integrated and link to the implementation; track unfinished integration in the repository.

## 5. Record and preserve
Record the decision, rationale, unresolved work and verification in the partner repository, distinguishing the user's reasoning from agent recommendations. Keep a brief choice, status and useful links on the canvas, with links back to the exploration from the repository record.

Preserve alternatives as browsable history. When archival is within the requested scope, follow the Scratchpad and Archive policy: retain the coherent group and its original owner, check dependencies and repair affected links. Otherwise leave it in place; choosing or integrating an option is not a request to archive or delete it. Deliberately deferred work can be marked Parked without implying rejection.

Report the question, the choice or open status, what was integrated and checked in Workshop, and links to the exploration and repository record.
