---
name: setup-wireframe-workflows
description: "Adopt Wireframe Workflows in a project and set up its design file: the standard pages, the Cover, page order and the design tool used. Use when starting a wireframe file, reorganizing an existing file into the standard pages, or adopting this collection in a project."
---

# Setup Wireframe Workflows
Set up a project to use this collection and give its design file the standard structure. The pages, how they work together and what the skills need from a design tool are defined once in the [collection README](../README.md); read it first.

## Scope and authority
Read the project's instructions first; they override these defaults. A setup request covers adopting the collection locally and setting up the named design file. It does not cover publishing, pushing, changing who can access the file, or deleting anything.

A design file is usually shared, and many design tools apply changes immediately with no undo for collaborators. Inspect the file read-only, then show the user the exact pages you will add, rename or reorder, and what the Cover will say, before changing anything. Never delete pages or boards, or move existing boards between pages, unless the user asks for that specifically.

## 1. Adopt the collection
Skip this when the project already pins the collection; use `update-wireframe-workflows` to change an existing adoption instead.

1. Inspect the project's Git state, existing submodules and current instructions. Preserve concurrent work.
2. Add the collection as a root-level submodule from its public URL, then create a project branch inside it from `main`:

   ```sh
   git submodule add -b main https://github.com/jcklpe/wireframe-workflows.git wireframe-workflows
   git -C wireframe-workflows switch --no-track -c project/<project-slug> main
   ```

3. Record the project branch in `.gitmodules`, follow the project's commit policy, and never push. A local branch is not available to collaborators until someone publishes it.

## 2. Record the project's choices
Add a short "Wireframes" section to the project's instructions, usually `AGENTS.md`, with:

- the design tool and the skill that operates it, for example Penpot through Agent Hands' `use-penpot`;
- a link to the hosted design file;
- any page names that differ from the standard ones, mapped to their standard roles;
- a pointer to this collection's README for page purposes and agent boundaries.

Keep identifiers out of the section if the repository is public and the user has not agreed to publish them.

## 3. Check the design tool
Read the tool skill and confirm it explains how to do each item in [what the skills need from a design tool](../README.md#what-the-skills-need-from-a-design-tool). Then confirm the agent can reach the intended file with one read-only call, for example by reading the file's name and its list of pages. Report any capability the tool lacks; the affected steps fall back to the user doing them by hand.

## 4. Set up the pages
1. Read the file's current pages and what is on each, without changing anything.
2. Map existing pages to the standard roles. An existing page that already does a standard page's job keeps its content; propose a rename only if the user wants standard names.
3. Propose the changes as one short list: pages to add, pages to rename, the new order, and the Cover's text. Wait for the user's approval.
4. Make the approved changes through the tool skill. Add missing pages empty, apart from the Cover.
5. Write the Cover: the file's name and purpose in one or two sentences, one plain line per page, and start links into Prototype and Showroom once they have content. Use the tool's ordinary text and links, not a template image.

## 5. Verify and report
List the pages again and compare them with the approved plan. Export the Cover as an image and check that it reads clearly. Report what was added, renamed and reordered, what is still empty, any capability gaps from step 3, and anything left unpublished, such as the collection's project branch.
