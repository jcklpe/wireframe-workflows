---
name: setup-wireframe-workflows
description: "Adopt Wireframe Workflows in a project, link the project to its cloud design files, and set up a file's standard pages, Cover and page order. Use when starting a wireframe file, reorganizing an existing file into the standard pages, connecting a repository to a design file, or adopting this collection in a project."
---

# Setup Wireframe Workflows
Set up a project to use this collection and give its design file the standard structure. The pages and their rules are defined in [pages and agent boundaries](../policies/pages.md); what the skills need from a design tool and the manifest format are in the [collection README's references](../README.md#references). Read both first.

## Scope and authority
Read the project's instructions first; they override these defaults. A setup request covers adopting the collection locally and setting up the named design file. It does not cover publishing, pushing, changing who can access the file, or deleting anything.

A design file is usually shared, and many design tools apply changes immediately with no undo for collaborators. Inspect the file read-only, then show the user the exact pages you will add, rename or reorder, and what the Cover will say, before changing anything. Never delete pages or boards, or move existing boards between pages, unless the user asks for that specifically.

## 1. Adopt the collection
Skip this when the project already pins the collection; use [update-wireframe-workflows](../update-wireframe-workflows/SKILL.md) to change an existing adoption instead.

1. Inspect the project's Git state, existing submodules and current instructions. Preserve concurrent work.
2. Add the collection as a root-level submodule from its public URL, then create a project branch inside it from `main`:

   ```sh
   git submodule add -b main https://github.com/jcklpe/wireframe-workflows.git wireframe-workflows
   git -C wireframe-workflows switch --no-track -c project/<project-slug> main
   ```

3. Record the project branch in `.gitmodules`, follow the project's commit policy, and never push. A local branch is not available to collaborators until someone publishes it.

## 2. Link the project to its design files
Create or update `design-files.json` at the root of the folder the design work belongs to, usually the repository root, in the [manifest format](../README.md#linking-a-project-to-its-design-files). Record each design file the project uses: its name, tool, URL and file ID, and where the project keeps local copies. Fill in the page roles in step 4. Preserve existing entries and any existing tool-specific manifest, such as a token export manifest; point to it from `local` rather than duplicating it.

Add a short "Wireframes" section to the project's instructions, usually `AGENTS.md`, that points to the manifest, names the skill that operates each tool (for example Penpot through Agent Hands' `use-penpot`), and tells agents to read this collection's policies in `wireframe-workflows/policies/` before changing the design file. Project-specific variations go in the project's own policies.

Ask before committing file identifiers to a public repository if the user has not already published them.

## 3. Check the design tool
Read the tool skill and confirm it explains how to do each item in [what the skills need from a design tool](../README.md#what-the-skills-need-from-a-design-tool). Then confirm the agent can reach the file named in the manifest with one read-only call, for example by reading the file's name and its list of pages, and check that the name matches the manifest. Report any capability the tool lacks; the affected steps fall back to the user doing them by hand.

## 4. Set up the pages
1. Read the file's current pages and what is on each, without changing anything.
2. Map existing pages to the standard roles. An existing page that already does a standard page's job keeps its content; propose a rename only if the user wants standard names. When several people will design in the file, propose a Workshop and Scratchpad for each, named for them, plus a Staging page, and record the owners in the manifest. Map an existing Archive as shared; create one only when historical material is ready to be filed there, placing it last. Preserve the original owner within each archived group, following [Scratchpad and Archive](../policies/scratchpad-and-archive.md).
3. Propose the changes as one short list: pages to add, pages to rename, the new order, and the Cover's text. Wait for the user's approval.
4. Make the approved changes through the tool skill. Add missing pages empty, apart from the Cover. Record the final page name for each role in the manifest's `pages`.
5. Write the Cover: the file's name and purpose in one or two sentences, one plain line per page, start links into Prototype and Showroom once they have content, and a link back to the project repository. Use the tool's ordinary text and links, not a template image. When the tool can store file metadata, also record the repository's address in the file.

## 5. Verify and report
List the pages again and compare them with the approved plan and the manifest's `pages`. Export the Cover as an image and check that it reads clearly. Report what was added, renamed and reordered, what is still empty, any capability gaps from step 3, and anything left unpublished, such as the collection's project branch.
