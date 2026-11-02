---
name: audit-wireframe-consistency
description: "Audit connected wireframe routes against agreed patterns, component usage and recorded decisions. Use when asked to find drift, check whether a change reached all relevant states, or review consistency across a Workshop."
---

# Audit Wireframe Consistency
Compare actual wireframes with the project's agreed design and connected behavior. Read the target project's instructions, manifest and current decisions, then [page boundaries](../policies/pages.md), [Workshop](../policies/workshop.md), [naming and layout](../policies/board-numbering-and-layout.md) and [verification](../policies/verification.md). Use the selected tool's skill for inspection.

## Scope
An audit is read-only unless the user also authorizes corrections. Work within the named owner, pages and routes; reading another contributor's work does not authorize changing it. Differences can be deliberate, unresolved or accidental. Do not invent agreement from visual similarity, recency or an agent-created status label.

## Procedure
1. **Bound the review.** Identify the requested routes or pattern, applicable decisions and available revision. Use the launcher and existing route record to establish entry contexts and affected states. State coverage limits; do not turn a focused audit into a whole-file redesign.
2. **Compare the implementation.** Inspect equivalent controls, component identities and variants, content, state handling, overlays, returns and shared consumers. Check that interaction changes preserve unrelated content and mode. Follow cross-route dependencies rather than inspecting only the showcase screen. Check layout, naming and launcher records when they are in scope.
3. **Classify findings.** Separate drift from an agreed decision, intentional variation, missing design, unresolved disagreement and prototype limitation. Cite the relevant decision and concrete board/state evidence. If the governing choice is unclear, identify it as a question rather than choosing a preferred contributor's work.
4. **Present actionable results.** Group related findings by cause or shared fix. Give each a useful reference, affected locations, user consequence, observed versus expected behavior, evidence type and a bounded recommendation. Identify what was sampled and what was not checked. Reuse existing QA records; do not manufacture issues or acceptance.
5. **Hand off corrections.** If fixes are authorized, use [fix-wireframe-bug-reports](../fix-wireframe-bug-reports/SKILL.md) for bounded defects or [build-wireframes](../build-wireframes/SKILL.md) for design work. Preserve the findings until each has a verified disposition. Record remaining consumers when a shared change is only partly integrated.

Use [audit-wcag](../audit-wcag/SKILL.md) for accessibility criteria, [check-implementation](../check-implementation/SKILL.md) for a built product and [merge-wireframes](../merge-wireframes/SKILL.md) for combining contributors' designs. This audit supplies evidence; human decisions about shared standards belong to the project's chosen governance.
