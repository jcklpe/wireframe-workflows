---
name: promote-wireframes
description: "Promote settled work from a wireframe file's Staging or Workshop into Prototype as a deliberate, checked step: verify states and links, copy the boards, save a named version, write a change note, flag affected Showroom screens and refresh the project's exports. Use when the user says a flow is done or asks to promote it to Prototype."
---

# Promote Wireframes
Copy settled work into Prototype, the page people and coding agents treat as the current design. The work comes from Staging when the file has one and from Workshop otherwise; the source keeps its boards, and Prototype is the cleaned-up version without dead ends or rough edges. Prototype changes only through this skill. Page rules are in [pages and agent boundaries](../policies/pages.md); the project's `design-files.json` names the file, its pages and where local copies live.

## Scope and authority
Promote only settled work: it passes the checks in step 2, and everyone whose work it includes agrees it is ready. Wait for approval of the plan in step 3. Changes to Prototype are shared and usually apply immediately, so check before copying anything and verify after. Never edit Prototype boards in place outside a promotion, and never delete boards; superseded work stays restorable through the file's version history. Showroom is curated for presenting to stakeholders, so promotion does not change it.

## 1. Identify what is being promoted
Name the flow or screens, list their boards in the source page, and find any Prototype boards they replace or connect to.

## 2. Check before copying
Check the source boards, and report every failure with the board it concerns:

- **States:** each screen has the states its flow needs, such as empty, loading, error and success, plus any the flow implies.
- **No dead ends:** every button and link leads to a board that will exist in Prototype after the copy, and every board is reachable from the flow's start.
- **Library use:** components come from the Component Library rather than local copies, and colors and type come from design tokens.
- **Example content:** made-up content follows the [example content policy](../policies/example-content.md).

Stop until each failure is fixed or the user explicitly accepts it as a known gap. Accepted gaps go into the change note. Run [audit-wcag](../audit-wcag/SKILL.md) as well when the project asks for it.

## 3. Propose the plan
Show the user one short list: the boards to copy, the Prototype boards they replace, links to update, Showroom screens the change affects, and the version name, such as "Promote: search results". Wait for approval.

## 4. Copy and connect
1. Copy the boards into Prototype through the tool skill. The source keeps its boards and carries on. Copies keep their board names, so later promotions replace the right boards; a copy that replaces an existing Prototype board takes its place and position, so links keep working.
2. Point the copies' links at Prototype boards instead of source ones, reconnect links from other Prototype boards, and set the flow's starting board.
3. Check again inside Prototype: every link resolves within Prototype, and nothing depends on Staging, Workshop, Scratchpad or Archive.
4. Lock the promoted boards when the tool supports it.

## 5. Record the promotion
- **Save a named version** with the name from the plan.
- **Write a change note:** which screens and states were added, changed or removed, the decisions behind them (linking any recorded decision notes), and any accepted gaps. Coding agents read this to know what to build next.
- **Flag Showroom:** list the Showroom screens that show something this promotion changed. Updating them is the user's choice, following the [Showroom policy](../policies/showroom.md).

## 6. Refresh the project's copies
Refresh the local copies listed in `design-files.json`, such as the native archive, image exports and design tokens, through the tool skill, and the specs through [spec-wireframes](../spec-wireframes/SKILL.md) when the project uses them, all from the promoted state. Use the change note as the body of the project's commit, follow its commit policy, and never push.

Report what was promoted, the checks and any accepted gaps, the version name, the flagged Showroom screens, what was refreshed, and anything left for the user to do by hand.
