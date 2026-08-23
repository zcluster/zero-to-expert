---
name: zero-to-expert
description: Build a concise, source-backed, highly visual standalone HTML atlas that helps a STEM-bachelor-level newcomer acquire an expert-grade map of an unfamiliar field. Supports user-selectable Lite mode (single-agent and fast) and Full mode (bounded multi-perspective research). Use for requests to enter, learn, understand, map, survey, master, or get up to speed on a new academic discipline, research area, technology, industry, market, or mixed domain; for newbie-to-expert guides, field primers, landscape reports, knowledge maps, and illustrated explainers; and when the user wants foundations, key concepts, major debates, value chains, milestones, current state, or latest developments organized into an HTML artifact.
---

# Zero to Expert

Create one self-contained HTML learning atlas, not a long chat answer. Optimize for mental-model formation, navigation, and evidence. Treat “expert” as an expert-grade map, vocabulary, and judgment framework—not a substitute for years of practice.

## Workflow

### 0. Freeze the output language and select the mode

- Read [references/language-routing.md](references/language-routing.md). Determine and freeze `content_language` from the user's original topic request before asking about execution mode.
- Language precedence is: an explicit output-language instruction; otherwise the dominant natural language of the original topic request; otherwise established user-authored conversation language. Ignore system locale, timezone, file paths, URLs, ambient context, skill/reference text, and the assistant's own prior wording.
- A language-neutral mode reply such as `Lite` or `Full` never changes `content_language`. Change it only when the user explicitly requests another output language.
- Read [references/modes.md](references/modes.md) and apply its budgets, localized selection prompt, and stopping rules.
- If the prompt already specifies Lite or Full, select it and proceed without another question.
- If the prompt does not specify a mode, pause before research or file creation and ask the user to choose **Lite (Recommended)** or **Full**, localized to `content_language`. Use a structured two-option user-input control when available; otherwise use the matching prompt in `references/modes.md`. Resume only after the reply.
- In a genuinely non-interactive execution environment that cannot receive a follow-up reply, use Lite and disclose the fallback.
- Mode changes breadth, parallelism, and artifact size—not citation rigor or factual standards.
- State the selected mode and `content_language` near the top of the HTML.

### 1. Frame the request

- Extract the topic, geography, time horizon, desired depth, and any explicit audience constraints without reopening the frozen language decision.
- Default to a reader with a STEM bachelor's degree, no domain knowledge, comfort with equations and charts, and limited time.
- Choose one route without blocking on clarification:
  - **Academic**: theories, mechanisms, methods, literature, open questions, or research frontiers dominate.
  - **Technology–industry**: products, engineering stack, manufacturing, firms, economics, ecosystem, regulation, or market change dominate.
  - **Mixed**: neither lens can explain the field alone. Use the stronger route as the spine and add clearly labeled modules from the other.
- State the classification, confidence, secondary lens, included/excluded scope, and evidence cutoff near the top of the HTML. If the user's wording is broad, choose a useful boundary and disclose it.
- Read [references/frameworks.md](references/frameworks.md) after classifying. Use only the selected framework sections plus the shared learning ladder.

### 2. Build a question tree before researching

- In **Lite**, build the question tree locally and never spawn subagents, even when delegation tools are available.
- In **Full**, read [references/multi-agent-orchestration.md](references/multi-agent-orchestration.md). Include `content_language` in the shared brief, use no more than three research subagents at once, and keep final language ownership with the main agent. If delegation is unavailable, apply the same bounded lanes sequentially.
- In either mode, the main agent owns scope, synthesis, the claim ledger, and the final HTML.

Answer these questions in notes before drafting:

1. What is the field, what is outside it, and why does it matter?
2. What 5–9 concepts explain most of the field?
3. What causal system, stack, or process connects those concepts?
4. Which distinctions prevent common beginner errors?
5. How did the field reach its current state?
6. Who or what are the canonical schools, methods, architectures, organizations, or products?
7. What is settled, contested, uncertain, or rapidly changing?
8. What do experts measure, compare, and argue about?
9. What should the reader study or do next to become operational?

Use the tree to avoid encyclopedia-style coverage. Prefer explanatory leverage over completeness. When using subagents, merge their outputs into one dependency-aware question tree before broad research begins; do not concatenate their lists.

### 3. Research and synthesize

- Read [references/research-quality.md](references/research-quality.md) before browsing or citing.
- Browse whenever the atlas includes “current,” “latest,” organizations, market data, standards, regulations, products, or fast-moving research. Do not rely on memory for unstable facts.
- Start broad enough to discover the field's vocabulary, then search by the question tree. Prefer primary and authoritative sources.
- Separate foundational knowledge from current developments. Attach exact dates to the latter.
- Triangulate consequential or disputed claims. Mark inference, uncertainty, and forecasts explicitly.
- Maintain a claim ledger while researching: claim, significance, source, publication date, event/data date, confidence, and destination section.
- In **Lite**, perform one bounded research pass guided by the local question tree.
- In **Full**, use at most one bounded parallel evidence wave when the branches are cleanly separable. Require claim-level source records; the main agent deduplicates sources, resolves disagreements, and assigns final claim IDs.
- Record the perspective or incentive of sources that are vendors, companies, industry associations, governments, advocacy groups, or consultancies. Use them for what they can directly establish and add independent context where stakes are high.
- Compress findings into models, contrasts, mechanisms, and examples. Do not paste research notes into the artifact.
- Do not ask subagents to generate separate HTML pages or independent complete atlases. Parallelize discovery and evidence collection; centralize narrative, visual design, citations, and artifact production.

### 4. Design the learning progression

Use progressive disclosure:

- **60-second orientation**: definition, why it matters, scope, and one master visual.
- **10-minute foundation**: core vocabulary, first principles, and the field's central mechanism or stack.
- **30-minute system map**: components, relationships, history, schools/players, metrics, and tradeoffs.
- **Expert lens**: debates, failure modes, edge cases, frontier, and how experts evaluate claims.
- **Action path**: an AI-assisted 2-hour / 2-day / 7-day sprint, diagnostic self-check, curated next steps, and source trail. Use AI for explanation, drills, critique, counterarguments, and feedback; require the reader to verify consequential claims against sources and produce their own artifacts.

Introduce every technical term before using it. Pair abstraction with one concrete example. Put details behind expandable `<details>` blocks where possible.

### 5. Produce the HTML

- Use [assets/html-blueprint.html](assets/html-blueprint.html) as a component and styling reference; adapt the structure to the topic rather than filling it mechanically.
- Write all reader-visible atlas prose and the delivery message in the frozen `content_language`. Preserve source titles in their published language; on first use, include the standard English term when it improves transfer to literature or industry discourse.
- Keep the hero `<h1>` short and label-like, not sentence-like: no more than 12 CJK characters (excluding punctuation and spaces) or 8 words in space-delimited languages. Move the explanatory thesis into the lede below it.
- Keep the main shell centered with visible breathing room. Use a generous desktop maximum width around 1720 px plus a responsive total horizontal gutter of roughly 32–96 px; do not make the page edge-to-edge, and do not fall back to a narrow 1200 px column on ultrawide screens. Constrain prose line length inside the shell separately.
- Create a single standalone `.html` file with inline CSS and minimal inline JavaScript. Do not require a build step, CDN, external font, or remote image to understand the page.
- Make it responsive and accessible: semantic landmarks, visible focus states, high contrast, reduced-motion support, keyboard-safe controls, useful link text, and readable mobile layout.
- Meet the selected mode's content, source, and visual budgets. Choose information-bearing visuals for the topic, not decoration:
  - system/process/causal flow;
  - concept hierarchy or architecture stack;
  - timeline with turning points;
  - comparison matrix, 2×2, tradeoff chart, or value-chain map;
  - metric dashboard or evidence/confidence panel;
  - annotated worked example.
- Prefer HTML/CSS diagrams and inline SVG with labels. Every visual must have a caption or adjacent explanation stating what to notice.
- Wrap every wide table, timeline, or diagram in an explicitly scrollable container and make its scrollability visually discoverable on narrow screens. Never let a wide visual force body-level horizontal scrolling.
- Add a sticky section navigator, a reading-progress indicator, a “legend/how to read” block, and print styles.
- Separate every main chapter with a clearly visible full-width rule. Use a darker rule around 3 px rather than a faint 1 px hairline.
- Distinguish **foundation**, **current state**, **frontier**, **debate**, and **inference** with consistent visual labels.
- Cite claims near where they appear with numbered links. Require at least one direct citation or a clearly labeled multi-source inference for every current-state, frontier, debate, forecast, and quantitative card. End with a categorized source library containing title, publisher/author, year/date, source type, perspective, and direct URL.
- End with “What you can now explain,” “What still requires practice,” a short self-test with answers, and an AI-assisted 2-hour / 2-day / 7-day capability sprint:
  - **2 hours — map it**: reconstruct the core model and vocabulary from memory, then use AI to expose gaps.
  - **2 days — apply it**: complete two worked cases or comparisons, including a counterexample and source verification.
  - **7 days — defend it**: produce an independent analysis or build, ask AI to red-team it, and revise it with primary evidence.

### 6. Verify before delivery

- Confirm every major question in the question tree is answered or explicitly scoped out.
- Check that a newcomer can follow the first two layers without reading expandable details.
- Check that the expert layer contains evaluation criteria, tradeoffs, uncertainties, and failure modes—not merely more terminology.
- Search the output for unresolved template tokens, placeholder copy, unsupported superlatives, undated “latest” claims, broken anchors, and citation mismatches.
- Verify language conformance before delivery: the `<html lang>` value, title, hero, metadata, navigation, chapter headings, explanatory prose, action path, self-test, source annotations, and delivery sentence must use `content_language`. Source titles, proper nouns, code, equations, and standard technical terms may remain in their original language. If the language is wrong, correct the artifact before delivery.
- For English and Simplified-Chinese artifacts, run `scripts/validate_language_output.py <html-file> --expected en|zh-CN` after drafting. A failed check blocks delivery. For other languages, perform the same region-by-region inspection manually.
- Open or render the HTML when tools permit. Inspect desktop and 400 px mobile layouts, navigation, expandable sections, wide visuals, body-level overflow, contrast, and print behavior. Iterate on visible defects.
- Prefer previewing through a temporary server bound only to `127.0.0.1` rather than `file://` when browser device emulation or anchor testing is needed. Check the console after a clean reload and distinguish page-origin errors from extension noise. Stop the server after QA.
- Keep the artifact concise enough to finish. Apply the mode-specific length target in [references/modes.md](references/modes.md), excluding markup, CSS, JavaScript, and source URLs.

## Delivery

Name the artifact `<topic>-zero-to-expert.html` using a short filesystem-safe topic slug. Return a clickable absolute file link and one sentence describing the selected mode, classification, scope, and evidence cutoff date. Mention important evidence gaps; do not reproduce the HTML in chat.
