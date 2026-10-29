---
name: merge-wireframes
description: "Combine work from several people's Workshops into a wireframe file's Staging page, piece by piece: bring in work that does not overlap or is already agreed, fix agent drift with the owners, and hold back real disagreements until the people involved settle them. Use when teammates' Workshop work is ready to combine, or when asked to merge wireframes."
---

# Merge Wireframes
Combine work from several Workshops into Staging, where the combined design is checked before promotion. A merge is not one mechanical pass: some pieces can come in at once while others wait on a decision, so it happens piece by piece. Page rules, including owned pages and Staging, are in [pages and agent boundaries](../policies/pages.md), and building follows [working in Workshop](../policies/workshop.md). The project's `design-files.json` names the pages and their owners, and the tool skill handles the mechanics; where a tool cannot copy boards between pages, a person pastes them and the agent finishes the job.

## Scope and authority
Merge only what the owners say is ready, and change Staging only through this skill. Read every Workshop, but change one only with its owner's OK. Workshops keep their boards, so each person's own work survives the merge. The agent prepares, copies, relinks and checks; the people whose work is involved decide every conflict. The agent does not settle or mediate disagreements, and never picks a side.

## 1. Choose the smallest piece
Merge one flow or route at a time, starting with the smallest one that is ready. For each Workshop involved, list its boards for that piece and what they connect to in Staging and Prototype.

## 2. Compare and sort
Compare the Workshops' boards with each other and with what Staging and Prototype already have, and put every difference in one group:

- **No overlap:** each person's work adds something the others don't touch, such as two new routes that both start from a screen Prototype already has. Bring it in as it is.
- **Agreed difference:** the boards differ, but the people have already agreed which way to go, for example in a decision note. Bring in the agreed version.
- **Drift:** an accidental difference, usually from agents working separately. Examples are a local lookalike instead of a library component, a raw value instead of a token, different names for the same state, different wording for the same action, or a later decision missing from earlier screens. Propose a fix toward the Component Library, the tokens and the recorded decisions, and confirm it with the board's owner.
- **Disagreement:** the people chose genuinely different approaches to the same problem. Hold it back as step 3 describes.

When it is unclear whether a difference is drift or a disagreement, ask the owners rather than treating a choice as an accident. Compare shared parts by what they are, not by how they look: two buttons that match are not the same component unless both are instances of it.

## 3. Hold back disagreements
Leave both versions of a disagreement in their Workshops, and merge everything that does not depend on it. Show the people involved where the versions differ, with an exported image of each, and note what in Staging is waiting on their decision. Once they have decided, record the decision in a short note, as [explore-wireframe-options](../explore-wireframe-options/SKILL.md) does, and merge that piece on its next pass.

## 4. Bring the work into Staging
Copy the boards into Staging through the tool skill, keeping their names and noting on each which Workshop it came from. Point their links at Staging boards, connect the new work to what Staging already has, and apply the drift fixes the owners confirmed. Then check that every link resolves within Staging and that every state and route each Workshop had made it across.

## 5. Report
Report what was merged from which Workshop, each difference with its group and how it was resolved, the decisions recorded, the disagreements still held back and what waits on them, and what Staging still lacks. When everyone whose work is in Staging agrees it is settled, promote it with [promote-wireframes](../promote-wireframes/SKILL.md).
