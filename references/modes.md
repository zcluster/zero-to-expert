# Execution Modes

Mode controls runtime, breadth, and artifact size. It never lowers evidence quality.

## Selection

- Freeze `content_language` using [language-routing.md](language-routing.md) before presenting any mode text.
- Choose **Lite** for `lite`, 快速版, 轻量版, single-agent, or 不使用 subagent.
- Choose **Full** for `full`, 完整版, 深度版, 多视角, multi-agent, or equivalent wording.
- If neither appears, ask after the initial prompt and before any research or file creation. On every invocation also ask whether to include the optional knowledge graph. If mode is unresolved, present both choices together; if mode is already explicit, present only the graph choice. Use the template matching `content_language`:

### English

Please choose the production mode:

- **Lite (Recommended)** — One agent, one bounded research pass, and faster delivery.
- **Full** — Up to three research agents, multi-perspective cross-validation, and deeper coverage.

Please choose the visual map option:

- **Include graph (Recommended)** — Add an interactive concept-and-relationship map to the hero; generation and layout checks take slightly longer.
- **Omit graph** — Keep a text-first hero and finish faster.

### Simplified Chinese

请选择制作模式：

- **Lite（推荐）** — 单 Agent、一次限定研究，速度更快。
- **Full** — 最多三个研究 Agent、多视角交叉验证，内容更深入。

请选择知识图谱：

- **创建（推荐）** — 在 HTML 右上角加入可交互的概念关系图；生成和排版检查会稍慢。
- **不创建** — 保持文字优先的标题区，完成更快。

- For another `content_language`, translate the English template faithfully while preserving the Lite/Full labels, both recommended markers, and the stated tradeoffs.
- Prefer one structured control containing the unresolved mode question and the required graph question when the client exposes it. Otherwise ask both in one concise chat message. Do not begin work until the user answers every presented choice.
- A reply selects only the named production choices. Bare values such as `Lite`, `Full`, `yes`, or `no` do not change `content_language`.
- If the runtime is non-interactive and cannot accept a reply, fall back to Lite when needed, omit the graph, and explicitly disclose both choices.
- Do not infer Full merely because a topic is broad, mixed, current, or described as “newbie to expert.”
- Record `Mode: Lite` or `Mode: Full`, `Content language: <language>`, and `Knowledge graph: Included` or `Omitted` in the scope/evidence panel near the top of the atlas.

## Lite — default fast path

- Use the main agent only. Never spawn subagents.
- Build 8–12 governing questions locally, then run one bounded research pass.
- Target 8–14 unique, high-quality sources. Prefer sources that answer multiple governing questions.
- Build 6–9 main sections and 2–4 information-bearing visuals.
- Target about 2,000–3,500 words for space-delimited languages or 5,000–8,000 reader-visible characters for CJK-led pages.
- Omit optional deep dives and interactive calculators unless essential to understanding the field.
- Stop when all core questions have an adequately sourced answer and further research would mostly add examples or detail.

Lite is not an uncited summary. Browse and verify unstable claims, cite current and quantitative claims near their use, distinguish inference from fact, and retain the expert judgment layer.

## Full — explicit bounded deep path

- Use up to three perspective lanes and follow [multi-agent-orchestration.md](multi-agent-orchestration.md).
- Question discovery is a short, no-browse pass: 5–7 questions per lane, merged into 12–18 governing questions.
- Run at most one parallel evidence wave. Each lane may return 6–8 unique sources and 8–12 claim records.
- Target 18–28 unique sources after deduplication, 9–13 main sections, and 4–7 information-bearing visuals.
- Target about 3,500–6,000 words for space-delimited languages or 8,000–12,000 reader-visible characters for CJK-led pages.
- Allow one follow-up only for a named evidence gap or direct conflict. Do not start a second generic research wave.
- If a lane is slow, duplicates another lane, or exceeds its budget, stop waiting for it and let the main agent cover the remaining named gap.

Full aims for broader triangulation and stronger cross-lens synthesis, not exhaustive coverage.

## Shared non-negotiables

Both modes use the same Academic, Technology–industry, or Mixed classification; source hierarchy; claim ledger fields; citation rules; accessibility requirements; and desktop/mobile QA. Always attach an evidence cutoff date and disclose material gaps.

The graph choice is independent of mode. When included, follow [knowledge-graph.md](knowledge-graph.md) and count the graph as one information-bearing visual within the selected mode's existing visual budget.
