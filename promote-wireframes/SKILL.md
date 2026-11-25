---
name: promote-wireframes
description: "Promote settled work from a wireframe file's Staging or Workshop into Prototype as a deliberate, checked step: verify states and links, add or replace the boards, save a named version, write a change note, flag affected Showroom screens and refresh the project's exports. Use when the user says a flow is done or asks to promote it to Prototype."
---

# Promote Wireframes
Copy settled work into Prototype, the page people and coding agents treat as the current design. The work comes from Staging when the file has one and from Workshop otherwise; the source keeps its boards, and Prototype is the cleaned-up version without dead ends or rough edges. Prototype changes only through this skill. Page rules are in [pages and agent boundaries](../docs/agent-policies/RESPECT-PAGES-pages.md); the project's `design-files.json` names the file, its pages and where local copies live.

## Scope and authority
Promote only settled work: it passes the checks in step 2, and everyone whose work it includes agrees it is ready. Wait for approval of the plan in step 3. Changes to Prototype are shared and usually apply immediately, so check before copying anything and verify after. Never edit Prototype boards outside a promotion, and never remove a board. Replacing one, as step 4 does, keeps the board and changes what is in it; its earlier contents stay restorable through the version saved first. Showroom is curated for presenting to stakeholders, so promotion does not change it.

## 1. Identify what is being promoted
Name the flow or screens, list their boards in the source page, and find any Prototype boards they replace or connect to. Pair each replacement with the exact Prototype board it replaces; a matching name suggests a pair but does not settle it.

## 2. Check before copying
Check the source boards, and report every failure with the board it concerns:

- **States:** each screen has the states its flow needs, such as empty, loading, error and success, plus any the flow implies.
- **No dead ends:** every button and link leads to a board that will exist in Prototype after the copy, and every board is reachable from the flow's start.
- **Library use:** components come from the Component Library rather than local copies, and colors and type come from design tokens.
- **Example content:** made-up content follows the [example content policy](../docs/agent-policies/LABEL-EXAMPLES-example-content.md).

Stop until each failure is fixed or the user explicitly accepts it as a known gap. Accepted gaps go into the change note. Run [audit-wcag](../audit-wcag/SKILL.md) as well when the project asks for it.

## 3. Propose the plan
Show the user one short list: the boards to add, each Prototype board to be replaced with its replacement, links to update and any that would be lost, Showroom screens the change affects, and the version name, such as "Promote: search results". Wait for approval.

## 4. Copy, replace and connect
Everything goes through the tool skill. The source keeps its boards and carries on.

1. Copy new boards into Prototype. Copies keep their board names, so later promotions can find the boards they replace.
2. Replace existing boards, after saving a version of the file and locking it where the tool can. The Prototype board keeps its identity, so links, flow starting points and comments aimed at it keep working, and it keeps its lock and hidden state. Its name, contents, size and position come from the source. When something else points at a part inside the old board, such as a flow that starts there, retarget or remove that first. If the tool cannot replace a board this way, say so and ask the user to do it by hand.
3. Point the promoted boards' links at Prototype boards instead of source ones, connect new boards to the rest of Prototype, and set the flow's starting board.
4. Check again inside Prototype: every link resolves within Prototype, and nothing depends on Staging, Workshop, Scratchpad or Archive.
5. Lock the promoted boards when the tool supports it.

## 5. Record the promotion
- **Save a named version** of the promoted state, with the name from the plan.
- **Write a change note:** which screens and states were added, changed or removed, the decisions behind them (linking any recorded decision notes), and any accepted gaps. Coding agents read this to know what to build next.
- **Flag Showroom:** list the Showroom screens that show something this promotion changed. Updating them is the user's choice, following the [Showroom policy](../docs/agent-policies/CURATE-SHOWROOM-showroom.md).

## 6. Refresh the project's copies
Refresh the local copies listed in `design-files.json`, such as the native archive, image exports and design tokens, through the tool skill, and the specs through [spec-wireframes](../spec-wireframes/SKILL.md) when the project uses them, all from the promoted state. Use the change note as the body of the project's commit, follow its commit policy, and never push.

Report what was promoted, the checks and any accepted gaps, the version name, the flagged Showroom screens, what was refreshed, and anything left for the user to do by hand.
