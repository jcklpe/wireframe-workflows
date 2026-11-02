# Verification
Report the scope and kind of evidence behind a claim. “Checked” alone does not say whether an agent inspected links, looked at an export, exercised the prototype or received human acceptance.

- **Structural inspection:** identities, component references, state configuration and interaction destinations resolve. Reachability does not prove correct behavior.
- **Visual inspection:** rendered states have been examined for layout, content and styling. An image does not prove interaction behavior.
- **Prototype playback:** the named path has been exercised from its stated initial context, including relevant branches, returns and cancellation. Record simulations or tool limits.
- **Human acceptance:** record who accepted what scope when that agreement is actually given. Agent checks do not imply acceptance by other contributors.

Use the evidence needed for the change, not a mandatory checklist for every small edit. Record the affected boards/routes, date or available revision, result and remaining limits in existing project records. Distinguish inspected examples from complete coverage. If playback is unavailable, say what was inspected and what remains to try; do not claim a behavior passed from destination IDs alone.

An interaction should change what its action implies while preserving unrelated content and relevant caller state. Check entry context, editing mode, selections and return destination where the change could affect them. A shared overlay needs checks from its distinct caller contexts.

For shared components or patterns, identify the affected consumers and variants, migrate within the authorized scope, and verify representative behavior plus known exceptions. Account for remaining consumers and historical dependencies before retiring a component. A successful sample or a renamed master does not prove complete migration. Follow existing ownership and agreement boundaries; this policy does not establish a governance process or make an agent's consolidation a shared decision.
