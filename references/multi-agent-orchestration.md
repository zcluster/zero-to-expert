# Multi-Agent Perspective Protocol

Use this protocol only when **Full mode** is selected. Its purpose is bounded, broader perspective coverage—not multiple competing atlases.

## Contents

1. Routing decision
2. Shared brief
3. Perspective lanes
4. Required return schema
5. Central merge
6. Optional evidence wave
7. Speed and stopping rules

## Routing decision

Enter this protocol only after the mode router has selected Full from explicit user wording. A broad, mixed, or fast-moving topic never activates it by itself. Use up to three parallel lanes when they are meaningfully independent. If delegation is unavailable, run the same bounded lanes sequentially.

## Shared brief

Before delegation, freeze and give every subagent the same compact brief:

- exact topic and route: Academic, Technology–industry, or Mixed;
- frozen `content_language`; research-note language must not override the final artifact language;
- audience and target capability;
- geography, time horizon, and evidence cutoff;
- included and excluded scope;
- assigned lane and neighboring lanes it must not duplicate;
- output schema, item limits, and source expectations;
- instruction to return structured research notes, not prose chapters or HTML.

Do not delegate classification or final scope ownership. The main agent decides both.

## Perspective lanes

Choose three lanes that minimize overlap. Adapt their names to the topic.

### Academic route

1. **Foundations and mechanisms** — prerequisites, core objects, theories, causal mechanisms, canonical models.
2. **Methods and evidence** — experimental/computational methods, benchmarks, canonical results, replication, what counts as evidence.
3. **Critique and frontier** — competing schools, boundary conditions, failure modes, open questions, recent research.

### Technology–industry route

1. **Science and engineering** — technical foundations, architecture, production/operation, performance constraints.
2. **Industry and economics** — value chain, customers, products, profit pools, firms, metrics, adoption and cycles.
3. **Critical and external** — regulation, standards, geopolitics, safety, bottlenecks, disputed claims, scenarios, beginner misconceptions.

### Mixed route

Use the stronger route's first two lanes. Make lane 3 explicitly bridge scientific confidence, engineering feasibility, operational scalability, and commercial adoption.

## Required return schema

Ask each question-discovery subagent for valid JSON matching this shape, with 5–7 questions, no browsing, and no surrounding essay:

```json
{
  "lane": "science-and-engineering",
  "questions": [
    {
      "question": "What must the reader be able to explain?",
      "why_it_matters": "How this changes the mental model",
      "level": "orientation|foundation|system|expert|frontier",
      "importance": "core|supporting",
      "dependencies": ["earlier concept or question"],
      "search_terms": ["primary-source query"],
      "likely_visual": "flow|stack|timeline|matrix|dashboard|worked-example"
    }
  ],
  "blind_spots": ["important issue outside this lane"],
  "likely_disagreements": ["claim or framing that needs triangulation"]
}
```

Treat invalid JSON as recoverable: extract the intended fields once rather than spending repeated turns on formatting.

## Central merge

The main agent must merge before research or drafting:

1. Normalize terminology and convert questions to reader capabilities.
2. Deduplicate semantic equivalents; keep the version with greater explanatory leverage.
3. Preserve genuine disagreements as explicit research questions. Never average incompatible claims.
4. Check coverage across orientation, foundations, system, history, evidence/metrics, expert judgment, and frontier.
5. Add dependencies and order questions from prerequisite to synthesis.
6. Rank by importance, evidence availability, and value to the reader. Keep 12–18 governing questions; demote the rest to subquestions or scope them out.
7. Map each governing question to a section, likely visual, and evidence need.

The result is one question tree, not three appended lists.

## Optional evidence wave

After the merged tree exists, reuse the same lanes only when they still form independent research branches. Run at most one evidence wave. Give each lane non-overlapping governing-question IDs and request 6–8 unique sources and 8–12 bounded claim records:

```json
{
  "question_id": "Q07",
  "claims": [
    {
      "claim": "Atomic, testable statement",
      "significance": "Why it belongs",
      "source_title": "Direct source title",
      "source_url": "https://direct.example/source",
      "published": "YYYY-MM-DD",
      "event_or_data_date": "YYYY-MM-DD or period",
      "source_type": "paper|standard|filing|official-data|documentation|report",
      "perspective": "independent|vendor|government|association|consultancy",
      "confidence": "high|medium|low",
      "status": "foundation|current-state|frontier|debate|inference|scenario"
    }
  ],
  "counterevidence_or_gaps": []
}
```

The main agent verifies URLs and consequential claims, merges duplicate sources, resolves date conflicts, and creates the authoritative claim ledger. Subagent output is research input, not accepted evidence by default.

## Speed and stopping rules

- Prefer three broad lanes over one subagent per persona; extra agents increase duplication and synthesis cost.
- Give each lane 5–7 discovery questions, 6–8 unique evidence sources, 8–12 claim records, and a one-pass deadline. Follow up at most once and only for a named gap or conflict.
- Parallelize independent discovery and retrieval. Keep classification, merge, conflict resolution, claim IDs, narrative, citations, and HTML sequential under the main agent.
- Stop a lane when new questions or sources mostly repeat existing coverage.
- Never start a second generic research wave. If a lane is slow, duplicative, or over budget, stop waiting and let the main agent cover only the remaining named gap.
- If parallel results disagree on scope, return to the frozen shared brief; do not let subagents silently redefine the task.
- If coordination overhead approaches the expected research time, collapse to the single-agent path.
