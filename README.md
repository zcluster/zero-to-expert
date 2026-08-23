<div align="center">

# Zero to Expert

**Turn an unfamiliar field into a concise, source-backed, highly visual HTML learning atlas.**

<a href="README.zh-CN.md"><kbd>简体中文</kbd></a>&nbsp;&nbsp;·&nbsp;&nbsp;<strong>English</strong>

</div>

---

`zero-to-expert` is a cross-platform Agent Skill built on the open `SKILL.md` format. It works with Codex, Claude Code, OpenCode, WorkBuddy, and other Agent Skills-compatible tools. It is designed for readers with a STEM bachelor's-level background who need a coherent map of an unfamiliar field without already knowing its specialist vocabulary.

Instead of assembling search results into an encyclopedia-like article, it first classifies the topic as **academic**, **technology–industry**, or **mixed**. It then builds a standalone visual HTML atlas around governing questions, causal mechanisms, system structure, major debates, current developments, and the judgment methods experts use.

> “Zero to Expert” means acquiring an expert-grade map, vocabulary, and evaluation framework. It does not replace years of research, engineering, commercial, or regulatory practice.

### Demo

Explore the semiconductor-industry atlas generated with this Skill. Both files contain the same structure, evidence cutoff, citations, interactive yield model, and responsive visual system.

- [Open the English semiconductor-industry demo](demos/semiconductor-industry-en.html)
- [打开中文芯片行业 Demo](demos/semiconductor-industry-zh.html)

### What it does

- **Selects the right lens**: academic, technology–industry, or a deliberately composed mixed route.
- **Starts with a question tree**: identifies the 8–18 questions that govern the field before collecting evidence.
- **Builds capability progressively**: moves from a 60-second orientation to foundations, a system map, expert judgment, and an action path.
- **Explains mechanisms, not just terms**: shows how concepts connect, how the system behaves, where bottlenecks arise, and why tradeoffs exist.
- **Uses source-backed research**: verifies recent, quantitative, disputed, and predictive claims and cites them near their use.
- **Separates evidence states**: visually distinguishes foundations, current state, frontier, debate, inference, and scenarios.
- **Creates information-bearing visuals**: flows, architecture stacks, timelines, comparison matrices, value chains, metric panels, and worked examples.
- **Delivers one portable file**: produces a self-contained `.html` artifact with inline CSS and minimal JavaScript—no build step or external font required.
- **Is responsive and accessible**: includes sticky navigation, reading progress, keyboard focus, discoverable overflow, mobile layout, and print styles.
- **Freezes the prompt language before mode selection**: a Chinese topic request produces Chinese HTML; an English topic request produces English HTML. The mode question is localized, and a bare `Lite` or `Full` reply cannot switch the artifact language. Standard English terminology may accompany first mentions when useful.

### Lite and Full modes

When the prompt does not name a mode, the Skill freezes the output language from the topic request and asks the mode question in that language before research begins. For an English request, it uses:

- **Lite (Recommended)** — One agent, one bounded research pass, and faster delivery.
- **Full** — Up to three research agents, multi-perspective cross-validation, and deeper coverage.

A language-neutral answer such as `Full` selects only the execution mode; it does not change the frozen output language.

| | Lite | Full |
|---|---|---|
| Best for | A fast, reliable field map | Complex, disputed, or cross-disciplinary topics |
| Execution | One agent, one bounded research pass | Up to 3 research agents in parallel perspective lanes |
| Governing questions | 8–12 | 12–18 |
| Sources | About 8–14 high-quality sources | About 18–28 unique sources after deduplication |
| Main sections | 6–9 | 9–13 |
| Information visuals | 2–4 | 4–7 |
| Goal | Faster and more compact | Broader triangulation and stronger cross-lens synthesis |

Both modes use the same citation, verification, and factual-quality standards. Lite reduces breadth and artifact size—not rigor.

### Topic frameworks

#### Academic route

For topics dominated by theories, mechanisms, methods, literature, and open research questions—for example condensed-matter physics, CRISPR research, or causal inference.

It emphasizes:

- the field's object, boundary, and central questions;
- prerequisite and concept dependencies;
- first principles, models, equations, and limits;
- paradigms and competing explanations;
- methods, data, benchmarks, uncertainty, and replication;
- canonical results, turning points, and the current literature map;
- open questions, disputes, and how experts identify weak evidence.

#### Technology–industry route

For topics dominated by products, engineering stacks, manufacturing, supply chains, companies, economics, and policy—for example semiconductors, EV batteries, or the cloud-computing industry.

It emphasizes:

- customer needs, delivered value, and industry boundaries;
- technical foundations, stacks, interfaces, and bottlenecks;
- R&D, manufacturing, yield, reliability, deployment, and operations;
- products, use cases, and performance–cost tradeoffs;
- value chains, profit pools, competition, and durable advantages;
- industry metrics, cycles, standards, regulation, and geopolitics;
- recent progress, scenarios, and how experts evaluate vendor claims.

A mixed topic uses one route as the narrative spine and inserts only the necessary modules from the other.

### Compatible platforms and installation

The core Skill does not depend on Codex-specific behavior. Compatible Agent Skills runtimes can use `SKILL.md`, `references/`, and `assets/` directly. `agents/openai.yaml` only supplies optional Codex UI metadata and can be ignored by other platforms.

| Platform | User-level location or method | Invocation |
|---|---|---|
| Codex | `~/.codex/skills/zero-to-expert/` | `$zero-to-expert` or automatic natural-language selection |
| Claude Code | `~/.claude/skills/zero-to-expert/` | `/zero-to-expert` or automatic selection |
| OpenCode | `~/.config/opencode/skills/zero-to-expert/` | Natural-language selection or the Skill tool |
| WorkBuddy | Import a local Skill package from Experts・Skills・Connectors | Select, invoke, or let WorkBuddy trigger it automatically |

Lite always uses the current agent only. In Full mode, the Skill uses up to three research agents when the runtime supports multi-agent execution; otherwise, it runs the same perspective lanes sequentially.

Clone the repository into the directory for your platform:

```bash
# Codex
mkdir -p ~/.codex/skills
git clone https://github.com/Zcreatzy/zero-to-expert.git ~/.codex/skills/zero-to-expert

# Claude Code
mkdir -p ~/.claude/skills
git clone https://github.com/Zcreatzy/zero-to-expert.git ~/.claude/skills/zero-to-expert

# OpenCode
mkdir -p ~/.config/opencode/skills
git clone https://github.com/Zcreatzy/zero-to-expert.git ~/.config/opencode/skills/zero-to-expert
```

OpenCode also discovers `~/.claude/skills` and `~/.agents/skills`, so one installation can be shared with another tool. For WorkBuddy, import this repository directory or a packaged copy through the Skill management UI. Editions that support workspace Skills can also use `.codebuddy/skills/zero-to-expert/`.

To update, run this command with the directory you actually installed into:

```bash
git -C <your-install-directory>/zero-to-expert pull
```

### Usage

Minimal prompt (shown with Codex invocation syntax; on another platform, simply say “use zero-to-expert”):

```text
Use $zero-to-expert to help me understand the semiconductor industry.
```

Choose the fast path directly:

```text
Use $zero-to-expert in Lite mode to create an English HTML atlas of the quantum-computing industry.
```

Request deeper multi-perspective research:

```text
Use $zero-to-expert in Full mode to teach me computational neuroscience, focusing on research paradigms, evidence methods, and the last three years of frontier work.
```

You can also specify geography, time horizon, audience, exclusions, or questions that the atlas must answer. If you do not, the Skill chooses a useful boundary and discloses its scope, classification confidence, and evidence cutoff date near the top of the HTML.

### What the HTML contains

A typical atlas includes:

1. Topic framing, scope, route classification, selected mode, and evidence cutoff
2. A 60-second orientation and one master visual
3. Five to nine high-leverage concepts and commonly confused distinctions
4. The core mechanism, system architecture, technical stack, or value chain
5. Historical turning points and the problems they resolved
6. Methods, products, participants, metrics, and tradeoffs
7. Current state, recent progress, disputes, bottlenecks, and frontier scenarios
8. How experts detect bad assumptions, metric gaming, and overclaiming
9. “What you can now explain,” remaining practice requirements, and a scored self-test
10. An AI-assisted 2-hour / 2-day / 7-day capability sprint and a categorized source library

### Design principles

- **Explanatory leverage over coverage**: choose the few concepts that explain most of the field instead of pursuing encyclopedic completeness.
- **Facts, inferences, and forecasts stay separate**: dated evidence is not blended with scenarios.
- **Current information is verified**: recent products, markets, policy, standards, and research are not taken from model memory alone.
- **Citations live near claims**: consequential current-state, quantitative, disputed, and predictive claims require direct citations or labeled multi-source inference.
- **Visuals must teach**: decorative imagery does not count; every visual states what the reader should notice.
- **Final synthesis stays centralized**: in Full mode, subagents collect questions and evidence while the main agent owns scope, judgment, citations, and HTML design.

### Repository structure

```text
zero-to-expert/
├── SKILL.md                              # Core workflow and delivery contract
├── agents/openai.yaml                    # Optional Codex UI metadata
├── assets/html-blueprint.html            # Responsive HTML component/style reference
└── references/
    ├── modes.md                           # Lite / Full budgets and stopping rules
    ├── frameworks.md                      # Academic, industry, and mixed frameworks
    ├── research-quality.md                # Evidence, citation, and research-quality rules
    └── multi-agent-orchestration.md       # Parallel research protocol for Full mode
```

### Feedback and contributions

Use [Issues](https://github.com/Zcreatzy/zero-to-expert/issues) for bugs, real-world examples, layout defects, or framework proposals. For changes, validate the Skill and test a generated HTML artifact for desktop/mobile layout, citations, and body-level horizontal overflow.

<p align="right"><a href="#zero-to-expert">Back to top ↑</a></p>
