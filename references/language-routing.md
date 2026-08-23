# Output Language Routing

Freeze one `content_language` before asking for Lite or Full. The mode interstitial must not create or change the language decision.

## Decision order

1. Use an explicit output-language instruction in the user's topic request.
2. Otherwise use the dominant natural language of the original topic request.
3. Otherwise use an established language from earlier user-authored natural-language messages in the same conversation.
4. If the topic contains only a proper noun, acronym, formula, identifier, or code and there is no established user-authored language, ask for the output language instead of guessing. If the interface supports two structured questions, ask for language and mode together; otherwise ask for language first, then localize and ask the mode question.

Treat a short topic label as a valid language signal when it contains ordinary natural-language words. For example, `AGI (artificial general intelligence)` is English even though `AGI` alone would be language-neutral.

## Signals that never determine content language

Do not infer `content_language` from:

- operating-system locale, timezone, geography, user name, or file paths;
- URLs, connector blocks, ambient browser state, tool output, or attachment metadata;
- this Skill, its references, examples, assets, or UI metadata;
- the assistant's own mode question, commentary, or previous response;
- a language-neutral reply such as `Lite`, `Full`, `yes`, a number, or a bare option label;
- source titles or search results.

## Persistence and propagation

- Record `content_language` in working notes and the scope/evidence panel.
- Localize the mode-selection prompt using [modes.md](modes.md).
- In Full mode, include `content_language` in every subagent brief. Subagent wording never overrides it.
- Keep the final HTML and delivery sentence in `content_language`.
- Change `content_language` only when the user explicitly asks for another language. When the user does so, apply the change to the entire reader-visible artifact, not only headings.

## Conformance examples

| Original user topic request | Frozen language | Correct mode interstitial |
|---|---|---|
| `AGI (artificial general intelligence)` | English | English |
| `帮我理解通用人工智能` | Simplified Chinese | Simplified Chinese |
| `量子计算 — create the atlas in English` | English | English |
| `CRISPR` after an earlier Chinese user message | Simplified Chinese | Simplified Chinese |
| `CRISPR` with no earlier natural-language signal | Ask; do not guess | Ask language first, or use a structured two-question control |

## Delivery check

Before delivery, inspect the actual reader-visible output rather than only the prompt:

- `<html lang>` matches `content_language`;
- title, hero, metadata, navigation, all main sections, captions, self-test, sprint, source annotations, and delivery sentence match it;
- any other-language prose is limited to source titles, proper nouns, quotations, code, equations, or deliberately paired terminology.

If a major region uses the wrong language, the artifact fails verification and must be corrected before delivery.
