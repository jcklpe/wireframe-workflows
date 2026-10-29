---
name: check-implementation
description: "Compare a running product with its wireframe file's Prototype and specs, screen by screen and state by state, run the accessibility checks only a built product can show, and list each difference with evidence and the decision it needs. Use when something has been built from the wireframes, or when asked whether the build matches the design."
---

# Check Implementation
Close the loop from design to build. Coding agents build from the specs; this skill checks that what they built matches Prototype and says where it does not. Page rules are in [pages and agent boundaries](../policies/pages.md); the project's `design-files.json` names the design file, its pages and where its specs live, and the tool skill handles the mechanics on the design side.

## Scope and authority
Check the screens the user names, in a development or test environment they name. The check only reads: it changes neither the product's code nor the design file. Use the project's own test accounts and test data; never enter real credentials or personal data. On a live site, only look: never submit forms or change data. Don't file issues or message anyone about the results without the user's go-ahead.

Neither side is automatically right. Prototype is the agreed design, but a build can settle an open question or run into a real constraint, so differences are listed for the user to decide, not resolved silently in either direction.

## 1. Gather
- **The design:** the specs for the screens in scope, made by [spec-wireframes](../spec-wireframes/SKILL.md), and the Prototype version they came from. If Prototype has changed since, refresh the specs first or note the gap. Without specs, compare with the Prototype boards directly.
- **The product:** its address, how to start it, and how to reach each state, such as test data that produces no results or a way to trigger an error.
- **Accessibility:** the list of checks for the built product from [audit-wcag](../audit-wcag/SKILL.md), when an audit was run.

## 2. Walk each screen
Open each screen at every viewport its spec covers, reach each of its states, and compare with the spec section by section:

- **Route:** the screen is at the spec's route.
- **Layout and components:** the regions appear in order and use the named components, and colors, type and spacing match the named tokens.
- **States:** each state exists and shows what the spec says. A state you cannot reach is "not reached", not a pass.
- **Interactions:** each control does what the interactions table says and leads where it says.
- **Content and data:** interface text matches exactly, and each field shows its data in the specified format. Example content from the design does not appear as real data.

Wireframes are not pixel specifications. Report a visual difference only when it changes meaning, breaks a token or affects use. Take a screenshot as evidence of each difference, kept outside the repository unless the user asks.

## 3. Run the built-product checks
Check what only a running product can show, citing each criterion:

- Everything works with a keyboard alone ([2.1.1](https://www.w3.org/TR/WCAG22/#keyboard)), focus moves in the reading and task order ([2.4.3](https://www.w3.org/TR/WCAG22/#focus-order)) and stays visible ([2.4.7](https://www.w3.org/TR/WCAG22/#focus-visible)).
- Controls expose a name, role and state to assistive technology ([4.1.2](https://www.w3.org/TR/WCAG22/#name-role-value)); read them from the accessibility tree.
- Text zoomed to 200% loses nothing ([1.4.4](https://www.w3.org/TR/WCAG22/#resize-text)), content reflows at 320 CSS pixels wide ([1.4.10](https://www.w3.org/TR/WCAG22/#reflow)), and wider text spacing breaks nothing ([1.4.12](https://www.w3.org/TR/WCAG22/#text-spacing)).
- Content that appears on hover or focus can be dismissed and stays while the pointer is over it ([1.4.13](https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus)).
- Rendered text still reaches the contrast that the audit measured from the tokens ([1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum)).

## 4. Sort the differences
Put each difference in one group:

- **The build differs from the design:** usually a fix for the coding agent.
- **The build settles an open question** from the spec: confirm the answer with the user, then record it in the design.
- **The build departs deliberately or does better:** the user decides whether the code changes or the design follows. A design change goes through [build-wireframes](../build-wireframes/SKILL.md) and [promote-wireframes](../promote-wireframes/SKILL.md), never by editing Prototype in place.

## 5. Report
Report, per screen and viewport, what matches and each difference: what the design says, what the product does, the evidence, its group and the decision it needs. Add the accessibility results and anything not reached. Write the code fixes as a list a coding agent can act on, and name the design changes the user has to decide on.
