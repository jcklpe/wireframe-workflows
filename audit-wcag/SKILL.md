---
name: audit-wcag
description: "Check wireframes against the WCAG success criteria a design can show, such as contrast from design tokens, target sizes, headings, form labels and errors, focus and alternative text, and record each result with its criterion. Use when asked to check accessibility in a wireframe file, or when a project requires an accessibility check before promoting work to Prototype."
---

# Audit WCAG
Catch accessibility problems while they are still cheap to fix. A wireframe shows some of what WCAG asks for, such as colors, sizes, structure, labels and states, but not how the built product behaves with a keyboard or a screen reader. The audit says which is which and never claims that the product conforms. Page rules are in [pages and agent boundaries](../policies/pages.md); the project's `design-files.json` names the file, its pages and its design tokens, and the tool skill handles the mechanics.

## Scope and authority
Audit the boards the user names, or the flow being promoted when [promote-wireframes](../promote-wireframes/SKILL.md) calls for it. Check against [WCAG 2.2](https://www.w3.org/TR/WCAG22/) level AA unless the project names another standard or level. The audit only reads: it changes no boards. Fixes are made in Workshop through [build-wireframes](../build-wireframes/SKILL.md), never in Prototype directly.

## 1. Gather
List the boards in scope, with every viewport and state. Read the design tokens with their resolved values, and the components the boards use. Note what the wireframes mark beyond what is visible, such as focus order, alternative text or heading levels.

## 2. Check
Check each board against the criteria below. Where tokens define a text and background pairing, check the pairing once, so every board that uses it passes or fails together.

| Area | What to check | Criterion |
| --- | --- | --- |
| Text contrast | Every text and background pair actually used reaches 4.5:1, or 3:1 for large text: at least 18pt (24px), or 14pt (about 18.7px) bold. Text in disabled controls and purely decorative text are exempt. | [1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum) |
| Non-text contrast | Input borders, focus indicators, meaningful icons and the parts of charts reach 3:1 against the colors next to them. | [1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast) |
| Use of color | Color is never the only signal for errors, links in text, status or required fields. | [1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color) |
| Target size | Everything that can be clicked or tapped is at least 24 by 24 CSS pixels, unless it is spaced well apart from other targets, sits inside a sentence, or has a full-size equivalent on the same screen. | [2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum) |
| Reflow | Narrow boards stack content into one column without sideways scrolling, apart from content such as maps or data tables that needs two dimensions. The criterion's test width is 320 CSS pixels; note it when the narrowest board is wider. | [1.4.10](https://www.w3.org/TR/WCAG22/#reflow) |
| Headings | Visible headings are marked as headings and describe their sections. A skipped heading level is worth fixing but is not a WCAG failure. | [1.3.1](https://www.w3.org/TR/WCAG22/#info-and-relationships), [2.4.6](https://www.w3.org/TR/WCAG22/#headings-and-labels) |
| Consistency | Navigation repeated across screens stays in the same order, and the same function has the same label everywhere. | [3.2.3](https://www.w3.org/TR/WCAG22/#consistent-navigation), [3.2.4](https://www.w3.org/TR/WCAG22/#consistent-identification) |
| Form labels | Every input has a visible label; placeholder text alone does not count. Required fields say so in text. | [3.3.2](https://www.w3.org/TR/WCAG22/#labels-or-instructions), [1.3.1](https://www.w3.org/TR/WCAG22/#info-and-relationships) |
| Errors | Error states exist, describe the problem in text and suggest a fix where one is known. | [3.3.1](https://www.w3.org/TR/WCAG22/#error-identification), [3.3.3](https://www.w3.org/TR/WCAG22/#error-suggestion) |
| Repeated entry | A flow does not ask for the same information twice without offering what was already entered. | [3.3.7](https://www.w3.org/TR/WCAG22/#redundant-entry) |
| Signing in | Signing in does not depend on remembering or solving something without an alternative, and allows pasting and password managers. | [3.3.8](https://www.w3.org/TR/WCAG22/#accessible-authentication-minimum) |
| Focus | Interactive components have a designed focus state that sticky headers or overlays never hide completely. Where the wireframe marks a focus order, it follows the reading and task order. | [2.4.7](https://www.w3.org/TR/WCAG22/#focus-visible), [2.4.11](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum), [2.4.3](https://www.w3.org/TR/WCAG22/#focus-order) |
| Dragging | Anything done by dragging can also be done with single taps or clicks. | [2.5.7](https://www.w3.org/TR/WCAG22/#dragging-movements) |
| Text alternatives | Meaningful images and icon-only buttons have marked text alternatives; decorative images are marked as decorative. | [1.1.1](https://www.w3.org/TR/WCAG22/#non-text-content) |

Measure contrast with the [WCAG contrast ratio](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio) from resolved color values. Blend a semi-transparent color with what is behind it first, and for text over an image, measure its worst area. WCAG sets no minimum text size, so mention very small text as advice, not as a failure.

## 3. Record the results
Give every check on every board one result:

- **Pass.**
- **Fail:** name the board, the element, what was found and what the criterion requires, for example "3.2:1, needs 4.5:1".
- **Not applicable:** the board has nothing the criterion covers.
- **Not shown:** the wireframe does not say enough to judge, such as an unmarked focus order. Either mark it in the wireframe or leave it for the built product.

Some criteria only the built product can show, such as keyboard operation, screen reader names and roles, zooming text to 200%, text spacing, and content that appears on hover or focus. List them once as checks for [check-implementation](../check-implementation/SKILL.md) rather than marking every board.

## 4. Report
Report the standard and level, the boards checked, each failure with its board and a suggested fix, the "not shown" items, and the list left for the built product. During a promotion, `promote-wireframes` stops until each failure is fixed or the user accepts it, and accepted failures go into its change note. After fixes in Workshop, audit the changed boards again.
