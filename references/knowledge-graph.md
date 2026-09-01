# Optional Knowledge Graph

Read this reference only after the user chooses to include the graph. The graph is a compact navigational model of the atlas, not a decorative network and not a substitute for the system diagram in the body.

## Content model

Derive nodes and edges from the final dependency-aware question tree and the atlas section plan. Do not invent a second taxonomy after research.

- Use 4–7 color-coded conceptual clusters. Color indicates cluster only; keep evidence states in the atlas's existing labels.
- Give every node a stable ID, concise reader-visible label, cluster, role, and destination section anchor.
- Use three visual roles: one central field/system node, larger core nodes, and smaller supporting or frontier nodes.
- Use only four relationship families: **prerequisite**, **part of**, **enables/causes**, and **constrains/trades off**. Explain them in a compact legend.
- Prefer labels of 2–5 words or at most 8 CJK characters. If a longer technical term is necessary, show a short label and expose the full term in an SVG `<title>` and accessible name.

### Density budgets

| Mode | Nodes | Edges |
|---|---:|---:|
| Lite | 12–20 | 14–28 |
| Full | 18–30 | 22–45 |

Treat these as ceilings, not targets. Keep total edges at or below roughly 1.6 times the node count. A non-central node should normally have no more than four visible connections. Remove redundant and merely associative edges. The reader should be able to answer “where do I start, what depends on what, and where is the frontier?” within ten seconds.

## Layout and placement

- Use a deterministic inline SVG with explicit coordinates. Do not ship a randomized force simulation: it makes screenshots unstable and commonly creates label collisions.
- Place the `<figure>` in the upper-right of a two-column hero. Give it approximately 38–46% of the hero width, a useful width of 380–640 px, and a 4:3 or 16:10 aspect ratio.
- Arrange concepts in readable tiers or cluster islands: prerequisites toward the upper/left area, the central model near the visual center, applications/outcomes toward the right, and frontier or constraints toward the lower edge when that ordering fits the field.
- Keep labels inside or immediately beside their nodes and manually inspect collision. Do not recreate the screenshot's hairball effect.
- At about 900 px and below, stack the graph below the hero copy at full width. Never let the SVG create body-level horizontal scrolling.
- When the graph is omitted, do not leave a blank column, placeholder, or empty card.

## Interaction and semantics

- Wrap the SVG in `<figure>` with a localized heading/caption that states what the reader should notice.
- Give the SVG `role="img"`, a localized `<title>`, and a short `<desc>` explaining how clusters and arrows work.
- Make nodes links to existing atlas section anchors whenever possible. Links must be keyboard focusable and have useful accessible names.
- On hover or keyboard focus, emphasize the selected node, its first-degree neighbors, and connecting edges; fade unrelated elements without hiding them. Reset on pointer exit or when focus leaves the graph.
- Provide a visible legend for cluster colors and relationship line styles. Do not rely on color alone.
- Respect `prefers-reduced-motion`. The graph must remain fully understandable with JavaScript disabled; interaction is enhancement only.

## Implementation contract

- Keep all SVG, CSS, and minimal JavaScript inline in the standalone HTML. Do not load D3, fonts, icons, or data from a CDN.
- Give each edge `data-from` and `data-to` values matching node `data-node` IDs so the small neighborhood-highlighting script can operate without a graph library.
- Use arrow markers sparingly and keep edge contrast subordinate to node labels. Differentiate a tradeoff/constraint edge with a dash pattern in addition to its label or legend.
- Use a consistent node radius scale; node size communicates structural role, not popularity or unsupported importance.
- Count the knowledge graph as one of the mode's visual-budget items. Do not reduce citation or core explanatory coverage merely to add it.

## QA checklist

- The central idea, starting concepts, and major clusters are evident without interaction.
- Every node ID and edge endpoint is unique and valid.
- Every linked section anchor exists.
- No important label overlaps another label, node, or hero text at the intended desktop width.
- Hover and keyboard focus produce the same neighborhood highlight.
- At a 400 px viewport the graph stacks, remains readable, and causes no body overflow.
- Print output shows the full graph and caption without clipping.
