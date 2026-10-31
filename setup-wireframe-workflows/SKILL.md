---
name: setup-wireframe-workflows
description: "Adopt Wireframe Workflows in a project, link the project to its cloud design files, and set up a file's standard pages, Cover and page order. Use when starting a wireframe file, reorganizing an existing file into the standard pages, connecting a repository to a design file, setting up a missing Figma/Penpot connector, or adopting this collection in a project."
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

## Optional global discovery
Offer the [global discovery procedure](references/global-skill-links.md) when requested or useful for work outside the current project. Ask for clients and skill selection, inspect existing destinations, preview with `scripts/link-skills.py`, then execute only the authorized selection. Keep project-local routing authoritative; do not automatically link nested Project Workflows or replace other installations.

## 3. Connect and check the design tool
Inspect the chosen agent client's existing plugins, MCP servers and tool skills before installing anything. Ask which client and design tool the person uses only when that is not already known. Reuse a working connection. If one is missing, guide setup rather than stopping at “connector unavailable.” Set up only the selected provider, preserve existing configuration, and have the user complete sign-in or secret entry through the provider's supported flow. Never ask for credentials in chat or store them in the project.

### Figma
Prefer the client's official Figma plugin when available; it supplies connector settings and tool skills together. Use the client's plugin discovery/install flow, or guide the user through installation and account authorization. If a plugin is unavailable, follow [Figma's current client-specific MCP setup instructions](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) for the supported remote or desktop connection and install the accompanying tool skills where required. Check the current instructions rather than assuming all clients use the same commands or support the same capabilities. Explain any client restart or session refresh needed, then retry discovery. An MCP entry alone does not prove canvas editing is available.

### Penpot
Use an installed `setup-penpot` skill when available. Otherwise offer the selected Penpot capability from [Agent Hands](https://github.com/jcklpe/agent-hands), reading its `setup-agent-hands/SKILL.md` and `setup-penpot/SKILL.md` before installation; do not assume the teammate has this checkout or install the entire capability catalog. That procedure owns runtime checks, protected local configuration, MCP client registration and verification. The [official Penpot MCP guide](https://help.penpot.app/mcp/) is the alternative for a directly supported client or when Agent Hands is unavailable. Guide the user through enabling MCP, configuring their chosen client and connecting the intended open file. A server URL containing a key is a credential; keep it out of tracked files and tool output. Preserve existing keys rather than rotating them as a routine setup step.

### Verify access and capabilities
Read the selected tool skill and check it against [what the skills need from a design tool](../README.md#what-the-skills-need-from-a-design-tool). Confirm tool discovery after any required refresh, then make one read-only call against the manifest's file, such as reading its name and pages, and compare the identity. Distinguish installation, authentication, file access and supported operations; tool listing alone does not prove file access. Diagnose missing account authorization, file permissions and unsupported operations separately. For missing file permission, tell the person what access to request from the owner without changing sharing yourself.

Continue repository onboarding while a user sign-in, client restart or access grant is pending. Leave a precise next step and a read-only verification to resume; do not replace the intended file or claim the connector is working. Unsupported operations may be completed manually. Connector setup does not authorize design changes; page changes still follow step 4.

## 4. Set up the pages
1. Read the file's current pages and what is on each, without changing anything.
2. Map existing pages to the standard roles. An existing page that already does a standard page's job keeps its content; propose a rename only if the user wants standard names. When several people will design in the file, propose a Workshop and Scratchpad for each, named for them, plus a Staging page, and record the owners in the manifest. Map an existing Archive as shared; create one only when historical material is ready to be filed there, placing it last. Preserve the original owner within each archived group, following [Scratchpad and Archive](../policies/scratchpad-and-archive.md).
3. Propose the changes as one short list: pages to add, pages to rename, the new order, and the Cover's text. Wait for the user's approval.
4. Make the approved changes through the tool skill. Add missing pages empty, apart from the Cover. Record the final page name for each role in the manifest's `pages`.
5. Write the Cover: the file's name and purpose in one or two sentences, one plain line per page, start links into Prototype and Showroom once they have content, and a link back to the project repository. Use the tool's ordinary text and links, not a template image. When the tool can store file metadata, also record the repository's address in the file.

## 5. Verify and report
List the pages again and compare them with the approved plan and the manifest's `pages`. Export the Cover as an image and check that it reads clearly. Report what was added, renamed and reordered, what is still empty, any capability gaps from step 3, and anything left unpublished, such as the collection's project branch.
