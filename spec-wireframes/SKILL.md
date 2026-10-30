---
name: spec-wireframes
description: "Write a structured spec for each Prototype screen in a wireframe file, covering purpose, route, components and tokens, states, interactions, copy and data fields, so coding agents can build from it, and keep the specs in the project's repository in step with Prototype. Use when Prototype screens are ready to build, when asked for specs or build instructions from the wireframes, or when a promotion refreshes them."
---

# Spec Wireframes
Turn Prototype screens into specs that coding agents can build from. People discuss the design from the wireframes themselves; coding agents get the same design as structured text they can follow exactly, with images for reference. Page rules are in [pages and agent boundaries](../policies/pages.md), and made-up content follows the [example content policy](../policies/example-content.md). The project's `design-files.json` names the file, its pages and where specs and image exports live, and the tool skill handles the mechanics.

## Scope and authority
Spec only Prototype screens, the cleaned-up version of the design. Workshop and Scratchpad are work in progress and not ready to build; Archive is historical evidence, not the current design. Read the design file but change nothing in it. Write the specs into the project's repository at the `specs` location in the manifest's `local`; when there is none, propose `specs/` beside the image exports and add it once the user agrees. Spec what Prototype shows, and write down anything it leaves unsettled as an open question rather than filling it in, because coding agents treat a spec as fact. Follow the project's commit policy, and never push.

## 1. Choose the screens
Spec the screens the user names. During a promotion, spec the promoted screens and any other screens whose links to them changed. A screen is the set of boards that share a flow and screen name across states and viewports, for example every "Orders · Order detail" board.

## 2. Read each screen
For each screen, read its boards, the components and tokens applied to them, the prototype links and where they lead, and all the text. Note the Prototype version name and any decision notes, flow maps and audit results the screen rests on. Use the image exports refreshed by the promotion, or export one image per state and viewport into the manifest's exports location.

## 3. Write one spec per screen
Write one Markdown file per screen, named after it, for example `orders-order-detail.md`. Start with a short block of fields, then use the same sections in every spec:

```markdown
---
screen: Orders · Order detail
flow: Check an order's delivery date
route: /orders/{order_id}
prototype_version: "Promote: order tracking"
boards:
  - name: Orders · Order detail · Loaded · Mobile
    image: ../exports/orders-order-detail-loaded-mobile.png
  - name: Orders · Order detail · Error · Mobile
    image: ../exports/orders-order-detail-error-mobile.png
---

# Order detail
## Purpose
## Layout and components
## States
## Interactions
## Content and data
## Accessibility
## Open questions
```

- **Purpose:** who uses the screen and what for, in a sentence or two, with links to the decision notes and flow map behind it.
- **Layout and components:** the screen's regions from top to bottom and the Component Library components in each, with how the layout changes between viewports. Name components and design tokens, not raw values, so the code follows the design system. A raw value with no token behind it is listed under open questions.
- **States:** each state, what causes it and what it shows, with its image.
- **Interactions:** a table of each control, what the person does and where it leads: another screen's spec, a state of this screen, or "outside this design".
- **Content and data:** the interface text exactly as written, and the data each field shows, with its format. Label example content as example, so it is never built in as real data.
- **Accessibility:** the screen's [audit-wcag](../audit-wcag/SKILL.md) results when one was run, including any accepted failures and its list of checks for the built product.
- **Open questions:** everything a builder needs that Prototype does not settle, such as an undecided route, a data source or behavior that no board shows, plus any gaps accepted during promotion.

## 4. Update the index
Keep an `index.md` in the specs folder that lists each flow with its starting screen and its screens in order, links every spec, and names the Prototype version the specs come from.

## 5. Check and commit
Compare each spec with its images, and follow every link in its interactions table to a spec or state that exists. Specs are rewritten from Prototype each time, so corrections go into the design, not into a spec by hand. When a spec's screen no longer exists in Prototype, ask before removing the spec. Commit the specs under the project's commit policy, together with the promotion's commit when one is running, and never push.

Report which specs were written or changed, what changed in them since the last version, since that is what coding agents act on, and the open questions they list.
