---
attention: live
reviewed: 2026-11-02
---
# Agent policy migration — Wireframe Workflows
Opened 2026-11-02. Stable slug: `agent-policy-migration`. [Tasks](agent-policy-migration.todo.md). This is a bounded receiving-project handoff; preparation changes no package, routing, policy status, tool, remote or design artifact.

## Ownership and current state
Preparation snapshot: repository `https://github.com/jcklpe/wireframe-workflows.git`; parent branch `main` at `1069577ea2cd4bcd6e3cbf94d6184f9293e6052c`. Selected child `project-workflows/` is `project/wireframe-workflows` at `c949eb8456e7712ec6bd6eaeedf5849557752c08`, clean at inspection, with the same recorded parent gitlink. Recheck this snapshot before acting; it is not a lock or a claim the checkout stays clean.

The declared policies are seven root policies/*.md documents, not docs/policies: board-numbering-and-layout, example-content, pages, scratchpad-and-archive, showroom, verification and workshop. They mix reusable design conventions and agent/page ownership boundaries; root skills refer to them.

Current policy inventory:
- `policies/board-numbering-and-layout.md`
- `policies/example-content.md`
- `policies/pages.md`
- `policies/scratchpad-and-archive.md`
- `policies/showroom.md`
- `policies/verification.md`
- `policies/workshop.md`

Related owners: [wireframe workflow foundations](wireframe-workflow-foundations.md). Those completed/adoption/design scopes retain their own remaining QA and closure decisions; this new receiving phase does not reopen or silently close them. Central coordination lives in Project Workflows, `docs/active-spikes/agent-policy-rollout.md` (prepared locally, not published). [Project instructions](../../AGENTS.md) remain authoritative.

## Project boundaries
This is the canonical Wireframe Workflows repository. Review which obligations govern agents and which design agreements govern everyone. Preserve the latter separately and keep skills tool-agnostic. Do not change actual design files, promote boards, alter another owner’s pages or migrate the nested Agentic Wiki checkout here. The nested copy currently has byte-identical seven policy bodies/AGENTS but a separate adaptation/history; deliver its reviewed source later through the Agentic Wiki owner, without redrafting the same policies independently.

Scoped local commits are permitted by AGENTS. Commit the workflow child before its exact gitlink here. Do not update containing configs or Agentic Wiki pins in this workstream; no push.

Keep secrets, private account/consent chronology, participant/course/meeting content and personal workspace paths out of public artifacts. Preserve actual private sources with their private owner before removal; public-safe sanitized originals alone are eligible for public retirement records. No service call, grant expansion, installation or browser fallback is authorized by this handoff.

## Target and decision boundary
Target the complete Project Workflows provider commit `79dddf9742c282d184c65d5c5ef87a142900897f`, not a moving main or the Agent Hands adaptation. This version provides create-agent-policy, edit-agent-policy, review-agent-policies, adopt-agent-policies and retire-agent-policy, with one shared format/checker/template implementation. The source and pilot commits are local-only at preparation; remote retrieval is not established.

The user authorized preparing this handoff, not applying this consumer migration or adopting unseen obligations. A later “pursue this spike” instruction starts its scoped work; it does not turn arbitrary quoted text, a saved proposal or a package update into adoption. Present the exact candidate set and rely on an actual human decision covering the kernel and substantive changes before marking adopted. Already-given relevant approval need not be requested again. Retain operative bodies while amendments are proposals; missing approval is a specific pending gate, not a reason to invent completion.

## Migration shape
Use YAML `---` frontmatter and meaningful verb–noun mnemonic IDs. Kernel policies use `type: kernel` and `_` before their unchanged IDs in filenames; ordinary agent obligations use `type: operational` without that prefix. Types, filenames and IDs confer no rank. Review prerequisites/related references for meaning, missing or inactive prerequisites, cycles and dependent impact; never infer edges from numeric order or settle contradictions by file order. Route AGENTS to the project-owned policy.index.md. Align documents.agent_policies and any legacy locator deliberately: keep separate human/design governance destinations where they remain meaningful, rather than mechanically pointing both keys at one folder.

Preserve original sanitized content, useful rationale and reserved legacy identities before recoverable removal. A human-owned index section may link retired records outside the flat active graph; it is not a live alias/supersedes chain. Never restore earlier private Git content just to preserve history. Remove an old directory only after every file has a reviewed current/historical owner, incoming live links are repaired and no unrelated/new concurrent file remains. Keep procedures with their actual skills and actual enforcement links honest; no policy edit changes a guard, grant or service permission.

## Verification and completion
Completion requires a reviewed old/new obligation mapping (or an explicit justified no-legacy-policy finding), recorded adoption decision or explicit human disposition, coherent actual routing/configuration, current index, valid graph/selected prerequisite closures, preserved sources and repaired links. Check actual files after application, repeat index generation and updater preview for no-op, and report exact child working/index/committed pins separately from parent pins. Run the selected tool with an existing Python 3.11+ and existing safe PyYAML or Ruby/Psych; do not install packages/environments for optional validation. If unavailable, report manual checks and the unrun graph tool honestly; do not certify an unchecked graph. Relevant provider tests are available under review-agent-policies/tests and update-project-workflows/tests; run focused suites for any actual provider defect fix, without adding prose-mirroring tests or running application builds for a docs-only change.

Exercise the five skills on real applicable migration operations and record which operations were actually needed; do not invent policies or retirements merely to tick five boxes. Semantic/authority review is separate from structural success. Receiving migration can complete before ordinary-use/client acceptance; keep a concrete remaining QA owner rather than claiming service/client compliance or keeping an unlimited hidden migration task. Preserve original task wording when moving each item to Done, and use the local closure/commit procedure rather than assuming a saved handoff is already closed.

## Deterministic delivery route
Read the selected [update procedure](../../project-workflows/update-project-workflows/SKILL.md), actual AGENTS and workflow.toml first. The target object was not present in this child at preparation. Obtain it through an authorized source route before preview. If using the user-designated canonical local provider, verify its repository/commit, then a bounded local `git -C project-workflows fetch --no-tags "$policy_source_checkout" 79dddf9742c282d184c65d5c5ef87a142900897f` imports Git objects without publishing or moving the working branch. Resolve that task-specific variable from an actual supplied/discovered project source; do not guess a personal path or create a permanent local-path remote. If no authorized source is accessible, report the exact missing object/source instead of silently substituting older remote main or using a browser.

Use the reviewed helper at the selected provider revision if the older installed helper is insufficient. From this repository, the default preview after the object is available is:

```sh
python3 -B project-workflows/update-project-workflows/scripts/update.py update --project . --revision 79dddf9742c282d184c65d5c5ef87a142900897f
```

Read the returned accepted SHA, focused review paths and proposed merge before applying. Use that exact SHA with `--apply` only after the launch/adoption/commit scope permits the operation; a divergent merge also needs the exact reviewed `--message` and only specifically reviewed `--reviewed` paths. Preserve every existing project/coordination/tooling value and copied-asset baseline. No reset, stash, arbitrary baseline fabrication or overwrite resolves a dirty/conflicting child. The updater supplies source, not adoption. After delivery load the five selected new policy skills; perform actual policy preparation/review/adoption separately. Keep child commits before the exact parent pin; a containing repository’s pin needs its own authorized owner. Nothing here authorizes a push or proves a fresh clone can retrieve local commits.

## Shared repository ordering
One canonical owner prepares the Wireframe policy/source decision. Agentic Wiki’s owner later reconciles the nested adaptation and exact nested pins after that commit is available through an authorized route. The two checkouts are distinct Git stores on different parent branches; do not edit both concurrently or bulk-copy adopted status between projects. The nested copy is a delivery target, not a second independent policy-authoring handoff.

## Receiving execution — 2026-11-02
The deterministic updater imported exact provider `79dddf9742c282d184c65d5c5ef87a142900897f` from the canonical local provider and merged it with the adaptation as `5acfd47627bdb04c091a7e11a097e9435a8549db`. Preview reported no focused overlaps, assets or baseline changes. Existing Python 3.14 was used after the default interpreter reported it was too old. No runtime was installed. Parent recorded/index gitlink remains `c949eb8456e7712ec6bd6eaeedf5849557752c08` pending the receiving checkpoint.

### Proposed obligation mapping
Keep the seven original shared design agreements in place, byte-for-byte, with their existing links. They govern design conventions shared by people and agents; do not reclassify them as agent-only governance or retire them. Seven new operational records in `docs/agent-policies/` require agents to apply those complete agreements within their scope and authorization. Three frozen kernel candidates come from the exact provider above. Procedures remain in their existing skills. No original identity is retired or reused; the Retire skill was reviewed but no retirement operation is appropriate.

| Existing agreement | Proposed agent ID | Preserved SHA-256 |
| --- | --- | --- |
| `board-numbering-and-layout` | `ARRANGE-BOARDS` | `cd1bc772f86aeb762d8bd7d21142969e8f3cb113c81612a45b3980ac72fe3904` |
| `example-content` | `LABEL-EXAMPLES` | `1d19048d73f7656660e0c4fc3393b07f6c790f83a3d871acbb619cd79849fdb2` |
| `pages` | `RESPECT-PAGES` | `b8e83324c4a8eee3ce69f746a94e4d50915dfa0c686017c120c64dd6fd44b294` |
| `scratchpad-and-archive` | `PRESERVE-EXPLORATION` | `aee9e4dea58e57cb43ada0a845bbdb10d679161f62570c2aa6c8e7bf772e4ddd` |
| `showroom` | `CURATE-SHOWROOM` | `bdbd558d4f4cafbf9b63f63af6b4174b533f1151d701ad493f19d226171e53bb` |
| `verification` | `REPORT-VERIFICATION` | `1ae99df87444f32dca9a2b03869b5147f1e7773f4ee66c8656e8aadfde0937fe` |
| `workshop` | `CONNECT-WORKSHOP` | `dc1ff7f6d4040f5e66de7d2c67e25cd503723a66898f98c7027b618de63a9193` |

Each operational record depends on ADOPT-POLICIES because it uses that policy's agent-only authority and policy/skill distinction. The kernel retains its source prerequisites; no artificial order between independent design agreements is introduced. The complete agreements remain the owners of design detail; no obligations are dropped through a summary. Proposed adoption includes all ten exact files, routing AGENTS to the project index, and setting the explicit agent-policy locator while preserving the separate shared-design locator. No candidate is adopted yet.

## Pending routing and consumer-boundary review
The current source updater skill says changed policies apply to new work. This cannot serve as automatic adoption of project-owned agent policies. Before migration completion, reconcile that sentence and the setup routing with explicit consumer-local adoption. Keep shared design agreement changes separately reviewed; agent policy source delivery must never imply consumer adoption. This is a concrete outstanding dependent, not a verified result.

Proposed AGENTS replacement for the first paragraph under Writing skills and policies:

> Agent-only obligations are indexed in [docs/agent-policies/policy.index.md](docs/agent-policies/policy.index.md). Read the applicable adopted policies and their complete prerequisite closure before work in scope; proposals are not operative. Shared design agreements remain in `policies/` and preserve their requirements for design work. Procedures live in the root skills and reference the applicable obligations and agreements rather than redefining them. Use the selected Project Workflows policy-management skills for policy changes. Package delivery does not adopt candidate policies or amend operative project copies.

Proposed configuration: retain `documents.agent_policies = "docs/agent-policies"`; change the stale `documents.policies = "docs/policies"` locator to `documents.policies = "policies"` for the actual shared agreement directory. This is an intentional local configuration change after the updater's mechanically preserved-values phase, not an upstream default or a fabricated baseline.

Proposed update-wireframe-workflows replacement for the Policies bullet:

> **Policies and design agreements:** delivery supplies candidate agent policies, not consumer adoption. Compare project-owned operative copies with their actual prior source and the incoming candidates; use the selected policy-management skills and an actual human adoption decision before changing operative obligations. Review shared design agreement changes separately and retain project ownership and authorization boundaries. Rework existing boards only when the user asks.

Setup must likewise route consumers to their actual project-owned agent-policy index after explicit adoption, while retaining shared design agreements and the target manifest/tool routing. Do not route consumer authority directly to proposed package source. Exact setup wording and README distinction remain to be prepared alongside the adoption decision.

### Remaining exact dependent candidates
Setup paragraph replacement:

Add a short "Wireframes" section to the project's instructions, usually `AGENTS.md`, that points to the manifest, names the skill that operates each tool (for example Penpot through Agent Hands' `use-penpot`), and identifies this collection's shared design agreements in `wireframe-workflows/policies/`. Preserve the target project's existing instructions and shared design agreements. For agent-policy adoption, use the target project's selected policy-management skills to compare the collection's candidates with its current obligations, preserve operative bodies, obtain an actual human decision covering the exact candidates, and maintain project-owned copies and their index. Route the project's instructions to that actual index and load applicable adopted prerequisite closures; do not route operative authority directly to the collection's proposed source. Report missing policy-management access and continue independent setup without inventing adoption. Project-specific variations remain project-owned.

README addition immediately below the Policies heading, retaining its seven-link list:

Shared design agreements in `policies/` retain the conventions and ownership boundaries for design work by people and agents. Agent-only obligations are indexed separately in [the project-owned agent policy index](docs/agent-policies/policy.index.md); each operational policy requires agents to apply the complete corresponding agreement within its scope. Root skills describe task procedures. Adopting projects review and adopt their own policy copies explicitly; receiving this package or passing a structural check does not adopt policies or authorize design-file changes.

The seven operational bodies are reviewable in the candidate files; all share the same authority/permission limits. Approval must cover the three kernels, seven operational records and the exact dependent wording before their operative adoption/routing transition. The receiving index must change its candidate notice to describe actual adopted status only after that decision.

## Adopted receiving result — 2026-11-02
Aslan approved the complete D1–D6 slate in the active chat. Applied all ten adopted records and approved dependent wording. The subsequent folder clarification authorized deletion only for obsolete duplicate documents; the seven originals hold the complete shared agreements and therefore remain. Agent-only records live in docs/agent-policies, not policies. Final child revision is `5f66dc1217e9771c175c4d5993595cb53148f3fd`; the receiving checkpoint records its exact gitlink. Prior candidate/pending sections above record the dated preparation sequence, not the current operative state. The task pair holds verification evidence and the remaining ordinary-use QA owner. Migration implementation is complete; formal archival remains separately authorized.
