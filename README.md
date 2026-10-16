# ReasonCore

**Critical Thinking & Decision Intelligence for AI Assistants**

ReasonCore is an open-source, portable [Agent Skills](https://agentskills.io/)-style instruction package for assistants that need to evaluate ideas, challenge assumptions constructively, compare alternatives, calibrate uncertainty, and recommend useful next steps.

> **Principle:** The goal is not to agree with the user or disagree with the user. The goal is to help the user reason and decide better.

## What it does

- Replaces automatic praise with evidence-based evaluation.
- Prevents reflexive criticism and performative skepticism.
- Accounts for constraints, opportunity costs, reversibility, and second-order effects.
- Separates facts, assumptions, predictions, and unknowns.
- Adapts effort to the stakes and complexity of the request.
- Encourages experiments, success metrics, and decision checkpoints.
- Includes domain playbooks and a reproducible evaluation protocol.

## Repository layout

```text
reasoncore/
├── SKILL.md                    # Main portable skill
├── references/                # Domain playbooks and decision tools
├── examples/                  # Worked examples
├── evals/                     # Evaluation prompts and rubric
├── .github/workflows/         # CI validation
├── scripts/                   # Local skill validator
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## Installation

### Agents supporting SKILL.md

Copy the `reasoncore` directory to the **skills directory recognized by your agent**. Paths and discovery behavior differ by product and version; consult your agent's current documentation. Enable or invoke `reasoncore` for evaluation and decision tasks. Keep the `references/` directory beside `SKILL.md` so referenced files remain accessible.

### Chat assistants without native skill loading

Copy the contents of `SKILL.md` into the assistant's project instructions or custom instruction field, subject to its character limits. Provide the reference files as knowledge/context when supported. This is an approximation of native skill loading, not an identical installation.

### API integrations

Include the main skill instructions in an appropriate developer/system message consistent with your provider's hierarchy. Retrieve relevant reference files only for applicable tasks. Do not allow untrusted user content to override trusted instructions.

## Usage examples

- “Evaluate this startup idea critically given my budget and time constraints.”
- “Review this architecture proposal and recommend a simpler alternative if justified.”
- “Challenge my assumptions and propose the cheapest useful experiment.”
- “Compare these career paths against my priorities; do not flatter me.”

ReasonCore does not need to be manually invoked for every simple question; it explicitly avoids unnecessary analysis.

## Evaluation

See [`evals/README.md`](evals/README.md). The included test cases are illustrative. **No unverified claims of 10×, 50×, or 100% accuracy are made.** Results depend on model, tools, context, domain, and evaluation design.

## Compatibility and limitations

The main `SKILL.md` uses a portable skill-folder convention. **Exact installation paths and support vary by agent.** It cannot override higher-priority instructions, grant tool access, supply missing evidence, or guarantee correctness. Professional advice still requires appropriate qualified oversight.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions should improve observable decision quality and include evaluation examples where possible.

## License

MIT — see [`LICENSE`](LICENSE).
