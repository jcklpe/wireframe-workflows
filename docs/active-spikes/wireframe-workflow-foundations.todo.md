---
attention: live
---
# Wireframe workflow foundations tasks
## Background
The [conceptual doc](wireframe-workflow-foundations.md) holds the adopted taxonomy, loops, provisional agent boundaries and open questions. This file tracks concrete work.

## Current state
The collection repository exists locally on `main`, adopts Project Workflows on the local branch `project/wireframe-workflows`, and is registered in the user's configs as a submodule tracking `main`. Nothing is published, and no skills exist yet.

## Public safety
This repository is public. Skills and examples use synthetic content; consuming projects keep their own design files, identifiers and private context.

## To Do
- Confirm the first skill's scope and name. The proposal is `structure-wireframes`: taxonomy, Cover page, page purposes and provisional agent boundaries.
- Draft `structure-wireframes/SKILL.md` with the skill-authoring guidance, keeping it tool-agnostic and plain-language. Validate its frontmatter and links.
- Answer the Penpot questions through `use-penpot`'s tooling: copying boards between pages, whether prototype links are limited to one page, and reading interactions for a dead-end check. Record the findings in Agent Hands, not here.
- Apply the taxonomy to the Landlord Mapper Wireframes file: add Cover and Prototype pages, move the current-state boards from Workshop to Prototype, and order the pages. This changes a shared design file, so it needs the user's OK; track it in that project's repository.
- Decide how a consuming project declares which pages its repository exports come from, alongside its existing export manifest.
- Write adoption instructions in the README once the first skill exists.
- Publication, which is the user's action: create the GitHub repository `jcklpe/wireframe-workflows`, push `main`, and push the `project/wireframe-workflows` branch to the Project Workflows remote. Then verify a fresh recursive clone, and publish the configs pin.

## Ready for Human QA
- Repository scaffold and Project Workflows adoption: review README, AGENTS and the workflow configuration.

## Done
- Created the repository on `main` with README, AGENTS, LICENSE (AGPL-3.0-only), an ignore baseline and TODO (`8168b1f`).
- Adopted Project Workflows from published `main` (`e173888`) on the branch `project/wireframe-workflows`, configured `workflow.toml` (`ce2c9bc` in the child), and pinned it (`faa2976`).
- Registered the collection in configs as a submodule tracking `main` (`b175374`), and added its routing row to configs' AGENTS (`de55f07`).
