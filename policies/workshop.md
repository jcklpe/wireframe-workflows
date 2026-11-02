# Working in Workshop
Workshop is the work-in-progress prototype. These rules apply to any change made there, by a person or an agent.

- **Read before changing.** Look at the screens and flows that exist, how they connect, and what the Component Library and design tokens offer before adding anything.
- **Ask rather than guess.** When a request leaves a design question open, ask it. When it has several reasonable answers, offer options in Scratchpad instead of picking one silently.
- **Reuse before inventing.** Build from Component Library components and the file's design tokens. A reusable part the library lacks is drafted locally in Workshop and proposed for the Component Library as a separate task. Matching someone else's style means using the same components and tokens, not copying how they look.
- **Keep one connected prototype.** Link each new screen into the working prototype. Every button and link leads somewhere or is clearly marked as not designed yet, and no board is left without a way in. Do not divide Workshop into containers by scenario, feature or development history by default. Keep individual screen/state boards; connected does not mean one giant screen.
- **Cover the states.** Consider what each screen shows when empty, loading, in error and successful, plus any state its flow implies. Build what is in scope and list the rest as open.
- **Work in small steps.** Edits are usually shared live. Describe larger changes before making them, and save a named version before a big batch.

Names follow the [naming rule](pages.md#naming), and made-up content follows the [example content policy](example-content.md).

## Launcher and entry points
Give each Workshop one cover-like launcher for entering and reviewing its connected prototype. The file Cover links to each Workshop launcher and may surface selected entries; it does not maintain a competing scenario directory. Keep prototype-only launcher access visually distinct from product navigation.

Each entry has a descriptive activity name and a direct prototype start link. Add a short starting context, a link or identifier for its user-flow scenario, and material unfinished or simulated behavior when relevant. A reviewer should know where to start, what to try and what limitations affect their conclusions. Several entries can start at the same screen under different conditions; scenarios need not partition the product into separate islands.

Starting an entry should establish its stated context. Reset relevant prototype state where supported; otherwise explain the necessary restart or setup. Do not silently inherit an unrelated session state or replace the page's content merely to reach a convenient demonstration.

Record the launcher and entries in the project's existing manifest or route record, including each entry's name, design-page/board reference, prototype link, scenario reference and relevant starting conditions. Use only applicable fields. Update that record and the launcher together when entries change. Link to detailed route coverage and verification in the repository rather than duplicating them on the canvas.

## Containers and shared routes
A container is a canvas organization aid, not a product screen or another navigation level. In Workshop, use one only for a concrete benefit that the connected layout and launcher do not provide, and record that reason briefly. Do not force shared screens into scenario ownership or duplicate them just to make groups self-contained. Scratchpad and Archive can group genuinely separate explorations and historical work under their own policy.

Use the tool's appropriate mechanism, such as a section or an organizing board. Check that nesting does not change clipping, prototype destinations, scrolling or exports. The container's descriptive title does not become a prefix in screen addresses or require its own numbering system.

## Checking work
Use [verification](verification.md) to report what was actually inspected and exercised. Resolved links, visual inspection, prototype playback and human acceptance are different kinds of evidence. A component or pattern change is complete only within its verified consumer scope; keep remaining migrations visible.
