---
name: update-wireframe-workflows
description: "Bring a project's adopted Wireframe Workflows up to date with shared main while keeping its own changes, update the project's pin, carry page, manifest and routing changes through to its instructions and design files, and contribute reusable improvements back. Use when the collection has improved and a project should catch up, or when a project's change should be shared."
---

# Update Wireframe Workflows
Bring a project's adopted copy of this collection up to date with shared `main` while keeping the project's own changes, then carry what changed through to the project's instructions and design files. A project adopts the collection as a pinned `wireframe-workflows/` submodule on its own `project/<project-slug>` branch, as set up by [setup-wireframe-workflows](../setup-wireframe-workflows/SKILL.md). The pages and their rules are in [pages and agent boundaries](../policies/pages.md); the manifest format and the design-tool capability list are in the [collection README's references](../README.md#references).

## Scope and authority
Read the project's instructions first; they override these defaults. An update request covers updating the project branch and the project's pin locally. It does not cover pushing, publishing, changing a shared design file without approval, deleting pages or boards, or rewriting history. Never reset, stash or force a checkout to make an update easier, and preserve concurrent work in both repositories.

## 1. Read the current state
1. In the project, check the Git status, the commit `wireframe-workflows/` is pinned to, and any uncommitted changes inside it.
2. In the collection, select the project branch recorded in `.gitmodules` and check that it contains the pinned commit; a submodule checkout often sits on a detached HEAD. If the branch is missing or does not contain the pin, stop and ask rather than recreating it.
3. Fetch shared `main` and find where it and the project branch last met:

   ```sh
   git -C wireframe-workflows fetch origin main
   git -C wireframe-workflows merge-base project/<project-slug> origin/main
   ```

## 2. Sort the changes
Compare that meeting point with `main` and with the project branch, across whole folders, and sort what you find into three groups:

- **Shared improvements** on `main`: new or changed policies, skills and references.
- **Project choices** on the project branch: changes that suit this project only. They stay on the project branch.
- **Conflicts**, where both sides changed the same rule or step. Show each one to the user and settle it with them; don't pick a side silently.

Read the commit messages and the diffs of `policies/`, the README's references and the skills. Note every change that reaches beyond the collection: a new or renamed page role, a new manifest version, a new design-tool capability, or new routing text for the project's instructions. Step 4 handles these.

## 3. Merge and pin
1. Merge `origin/main` into the project branch with an ordinary merge, which keeps both histories; a fast-forward is fine when the project branch has no changes of its own. Never reset the project branch to `main`.
2. Check the result: `main` is now an ancestor of the project branch, and every remaining difference from `main` is a project choice you can name.
3. Commit inside the collection first, then record the new pin in the project and commit that, following the project's commit policy. Never push.

## 4. Carry the changes through
Handle each change from step 2 that reaches beyond the collection:

- **Instructions:** if the routing text that setup adds has changed, update the project's "Wireframes" section to match, keeping its project-specific wording.
- **Manifest:** if the manifest format has a new `schema_version`, update `design-files.json` to it, keeping every existing entry and value.
- **Design tool:** if the capability list has grown, check that the tool skill explains each new item, as in setup's step 3, and report any gap.
- **Pages:** if page roles were added, renamed or redefined, read the design file and propose the changes as one short list, as in setup's step 4. Wait for approval, make the approved changes through the tool skill and record them in the manifest's `pages`. Never delete pages or boards, or move boards between pages, unless the user asks for that specifically.
- **Policies:** changed policies apply to new work. Summarize what now works differently; rework existing boards only when the user asks.

## 5. Share improvements back
When a change on the project branch would help every project, offer to contribute it. Rebuild it as a new commit on a clean branch from shared `main`, with nothing project-specific in it: no project names, file identifiers, page names or private notes. Never merge the project branch into `main`. Publishing that branch and merging it into `main` are the user's actions.

## 6. Verify and report
Check that the project pins the collection commit you made, that the project branch contains `main`, and that the manifest's `pages` still match the design file. Report the old and new collection revisions, the project choices kept, any conflicts and how they were settled, what changed in the project's instructions, manifest and design file, any tool capability gaps, and what remains unpublished. Collaborators cannot fetch the new pin until the collection's project branch is pushed, so it must be published before the project that pins it.
