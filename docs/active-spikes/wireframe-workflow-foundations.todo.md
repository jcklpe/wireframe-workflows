---
attention: live
---
# Wireframe workflow foundations tasks
## Background
The [conceptual doc](wireframe-workflow-foundations.md) holds the adopted taxonomy, loops, provisional agent boundaries and open questions. This file tracks concrete work.

## Current state
The collection is published at [jcklpe/wireframe-workflows](https://github.com/jcklpe/wireframe-workflows) on `main`, adopts Project Workflows on its published branch `project/wireframe-workflows`, and is registered in the user's configs as a submodule tracking `main`. Every planned skill exists as a draft awaiting the user's review.

## Public safety
This repository is public. Skills and examples use synthetic content; consuming projects keep their own design files, identifiers and private context.

## To Do
- In Agent Hands' `use-penpot`, explain how Penpot does each item in the README's design-tool list, under the same names. Answer the Penpot questions there: copying boards between pages, whether prototype links are limited to one page, and reading interactions for the state and dead-end checks.
- Explore how teammates coordinate in a shared file, and whether that needs its own skill.
- Apply the taxonomy to the Landlord Mapper Wireframes file: add Cover and Prototype pages, promote the current-state boards from Workshop into Prototype (copying them, so Workshop keeps them as the starting point for new work), order the pages, and add `design-files.json` to that repository, referencing its existing token export manifest. This changes a shared design file, so it needs the user's OK; track it in that project's repository.
- Decide how a project declares which pages its repository exports come from, in `design-files.json` or its tool-specific export manifest.
- Have `use-penpot` read `design-files.json` to find a project's file and page roles, and explain how Penpot stores file metadata for the link back to the repository.

## Ready for Human QA
- Policies: pages and agent boundaries (with naming), working in Workshop, Showroom and example content.
- README: policies, skills and references (the design-tool capability list and the `design-files.json` manifest), and adoption.
- `setup-wireframe-workflows` draft: adoption, linking the project to its design files through the manifest, routing agents to the policies, checking the design tool, setting up pages and the Cover, and verification.
- `build-wireframes` draft: the everyday loop that applies the policies: take the request, read the current state, choose the path (build, ask, map the flow, explore options or propose a Component Library part), build in Workshop, check, report and loop.
- `explore-wireframe-options` draft: framing the question, fair side-by-side options in Scratchpad, presenting trade-offs and waiting for the choice, folding it into Workshop, and recording and retiring the decision.
- `promote-wireframes` draft: checks before copying (states, dead ends, library use, example content), an approved plan, copying into Prototype with retargeted links, a named version, a change note, flagging affected Showroom screens, and refreshing the project's copies.
- `update-wireframe-workflows` draft: reading the pin and project branch, sorting shared improvements, project choices and conflicts, merging and pinning, carrying page, manifest, capability and routing changes through to the project with approval, sharing improvements back, and verification. Setup and the README link to it.
- `map-user-flows` draft: naming the goal and its sources, reading the existing route, an outline of steps, actions, branches and ends agreed before drawing, a plain flow map in Scratchpad marking existing, changed and new steps, and the hand-off to `build-wireframes`. `build-wireframes` and the README link to it.
- `audit-wcag` draft: a read-only check against WCAG 2.2 AA by default, covering what a design can show (contrast from tokens, use of color, target size, reflow, headings, consistency, form labels and errors, repeated entry, signing in, focus, dragging and text alternatives), each result recorded as pass, fail, not applicable or not shown with its criterion, and a list of built-product checks for `check-implementation`. `promote-wireframes` and the README link to it.
- `spec-wireframes` draft: one Markdown spec per Prototype screen for coding agents (fields, then purpose, layout and components, states, interactions, content and data, accessibility and open questions), an index, specs regenerated from Prototype rather than edited by hand, and unsettled details recorded as open questions. The README manifest gains an optional `specs` location; `promote-wireframes` and the README link to it.
- `check-implementation` draft: a read-only comparison of a running build with Prototype and its specs, screen by screen and state by state in a test environment, the accessibility checks only a built product can show, differences sorted into build fixes, settled open questions and deliberate departures for the user to decide, and a report with evidence. `audit-wcag` and the README link to it.
- Repository scaffold and Project Workflows adoption: review README, AGENTS and the workflow configuration.

## Done
- Settled the first skill set with the user: `setup-wireframe-workflows`, `build-wireframes`, `explore-wireframe-options`, `promote-wireframes`, `present-wireframes` and `update-wireframe-workflows`.
- Created the repository on `main` with README, AGENTS, LICENSE (AGPL-3.0-only), an ignore baseline and TODO (`8168b1f`).
- Adopted Project Workflows from published `main` (`e173888`) on the branch `project/wireframe-workflows`, configured `workflow.toml` (`ce2c9bc` in the child), and pinned it (`faa2976`).
- Registered the collection in configs as a submodule tracking `main` (`b175374`), and added its routing row to configs' AGENTS (`de55f07`).
- Published the collection: the user created `jcklpe/wireframe-workflows` and pushed `main` and the Project Workflows branch `project/wireframe-workflows`. A fresh recursive clone checks out both pinned commits, and the commit configs' published pin names is fetchable.
