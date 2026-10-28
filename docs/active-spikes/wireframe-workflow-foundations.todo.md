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
- Draft the remaining skills, one at a time and each reviewed by the user before committing, keeping them tool-agnostic and plain-language with the skill-authoring guidance. Validate frontmatter and links for each:
  - `build-wireframes`.
  - `explore-wireframe-options`.
  - `promote-wireframes`.
  - `present-wireframes`.
  - `update-wireframe-workflows`, mirroring `update-project-workflows`. Then link to it from `setup-wireframe-workflows`.
  - `map-user-flows`.
  - `populate-example-data`.
  - `audit-wcag`.
  - `spec-wireframes`.
  - `check-implementation`.
- In Agent Hands' `use-penpot`, explain how Penpot does each item in the README's design-tool list, under the same names. Answer the Penpot questions there: copying boards between pages, whether prototype links are limited to one page, and reading interactions for the state and dead-end checks.
- Explore how teammates coordinate in a shared file, and whether that needs its own skill.
- Apply the taxonomy to the Landlord Mapper Wireframes file: add Cover and Prototype pages, move the current-state boards from Workshop to Prototype, and order the pages. This changes a shared design file, so it needs the user's OK; track it in that project's repository.
- Decide how a consuming project declares which pages its repository exports come from, alongside its existing export manifest.
- Publication, which is the user's action: create the GitHub repository `jcklpe/wireframe-workflows`, push `main`, and push the `project/wireframe-workflows` branch to the Project Workflows remote. Then verify a fresh recursive clone, and publish the configs pin.

## Ready for Human QA
- README: page taxonomy, how the pages work together, agent boundaries, the design-tool capability list and adoption.
- `setup-wireframe-workflows` draft: adoption, recording the project's choices, checking the design tool, setting up pages and the Cover, and verification.
- Repository scaffold and Project Workflows adoption: review README, AGENTS and the workflow configuration.

## Done
- Settled the first skill set with the user: `setup-wireframe-workflows`, `build-wireframes`, `explore-wireframe-options`, `promote-wireframes`, `present-wireframes` and `update-wireframe-workflows`.
- Created the repository on `main` with README, AGENTS, LICENSE (AGPL-3.0-only), an ignore baseline and TODO (`8168b1f`).
- Adopted Project Workflows from published `main` (`e173888`) on the branch `project/wireframe-workflows`, configured `workflow.toml` (`ce2c9bc` in the child), and pinned it (`faa2976`).
- Registered the collection in configs as a submodule tracking `main` (`b175374`), and added its routing row to configs' AGENTS (`de55f07`).
