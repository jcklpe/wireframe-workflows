---
name: fix-wireframe-bug-reports
description: "Investigate and fix reported wireframe or prototype problems, such as incorrect navigation, lost editing state, clipped overlays or inconsistent controls. Use when the user points out a defect in chat, a screenshot or a walkthrough; do not require a report form."
---

# Fix Wireframe Bug Reports
Make the user's report actionable. Read the target project's instructions, design-file manifest and relevant decisions, then [page boundaries](../policies/pages.md), [Workshop](../policies/workshop.md) and [verification](../policies/verification.md). Use the selected design tool's skill for inspection and changes.

## Scope
A request to fix a reported problem authorizes a bounded correction within the user's existing scope. A question, discussion-only request or request to log it for later does not authorize a design change. Preserve other contributors' work; shared-library changes and Prototype promotion retain their existing boundaries. A bug report is not permission for a wider redesign.

## Procedure
1. **Locate and understand.** Infer the file, screen, starting state, action and expected result from the conversation, screenshot and connected routes. Ask only for missing information that materially affects diagnosis. Do not ask the user to fill out fields the agent can establish.
2. **Inspect and reproduce.** Trace the actual caller, state, target and return path. Exercise the behavior where possible; separate observed behavior from a likely cause. Compare with the agreed design. Distinguish a defect, an undesigned state, an unresolved design choice and a known prototype limitation.
3. **Make the bounded correction.** Follow the clear requested behavior or recorded decision. If alternatives require a design decision, present the specific choice and continue independent investigation. Check shared consumers before changing a component; use [build-wireframes](../build-wireframes/SKILL.md) for broader design work.
4. **Verify the consequence.** Recheck the reported path and affected neighboring states, including cancellation or return where relevant. Inspect the rendered result. Follow the verification policy and disclose untested behavior rather than treating a valid link as successful playback.
5. **Report and retain useful evidence.** Say what caused the problem, what changed, where to check it and what remains uncertain. Update the existing QA or work record when one owns the issue. Keep unresolved reports discoverable there; do not create a ticket for every small fix or publish external records without authorization.

Use [audit-wireframe-consistency](../audit-wireframe-consistency/SKILL.md) when the request is to look for drift across a wider set of routes. For a running product rather than wireframes, use [check-implementation](../check-implementation/SKILL.md).
