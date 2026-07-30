# Contributing to Guardian

Thank you for your interest in contributing. This document covers how to open issues, submit changes, and align with Guardian's development principles.

## Contribution Scope

This repository contains two distinct, historically separate bodies of work. Please state in your issue or PR which one you are contributing to:

- **Specification contributions** — changes to `specs/` (V0.2 Decision
  Equivalence, V0.3-mini/V0.3 Acceptance, V0.4 candidate) or to the
  research constitution described in the current `README.md`. This is
  Guardian's current research direction: cross-system comparison
  determination between independently governed judgments.
- **Historical runtime-prototype contributions** — changes to the
  executable Python package (`guardian/`), `ARCHITECTURE.md`,
  `docs/boundaries.md`, `docs/ecosystem_positioning.md`, `examples/`,
  or `tests/`. This code implements an earlier single-runtime
  intent → policy → ALLOW/DENY/ESCALATE authorization prototype,
  documented as historical in the files above (see
  `docs/reconciliation-items.md`).

The "Development Principles" section below applies to the historical
runtime-prototype code. It does not define requirements for
specification contributions, which should instead follow the
constitutional and comparison-semantics conventions already
established in `specs/`.

## Opening Issues

- Use the GitHub issue tracker for bugs, feature requests, and design discussions.
- For bugs: include steps to reproduce, expected vs actual behavior, and environment (OS, Python version).
- For specification features: identify the governance object, the
  comparison-layer question, the proposed invariant or decision rule,
  relevant failure semantics, and supporting evidence or test vectors.
- For historical runtime-prototype features: describe the use case and
  how it affects the intent → policy → ALLOW / DENY / ESCALATE flow.
- Check existing issues and discussions before opening a duplicate.

## Pull Request Guidelines

- Open a pull request from a branch (e.g. `feature/your-change` or `fix/issue-description`).
- Keep changes focused. One PR should address one logical change.
- For historical runtime-prototype changes, ensure tests pass by
  running `pytest tests/` from the repository root.
- For historical runtime-prototype changes, ensure the relevant
  examples still run:
  `python examples/demo.py`,
  `python examples/replay_demo.py`, and
  `python examples/agent_integration_demo.py`.
- Update documentation (README, ARCHITECTURE, or code comments) if behavior or APIs change.
- PR titles and descriptions should clearly state what is being changed and why.

## Development Principles (Historical Runtime Prototype)

These principles apply to the historical `guardian/` package described
above, not to the current specification work in `specs/`:

- **Deterministic decisions** — The decision path must remain deterministic for a given intent and policy. Avoid introducing non-determinism in the Policy Engine, Decision Engine, or Permission Model.
- **Policy as code** — New behavior should be expressible via policy rules where possible, rather than new hardcoded branches. Extend the policy schema or loader instead of special-casing in code when feasible.
- **Replay verification** — Evidence ledger format and hash chain semantics must stay consistent so that replay and ledger validation remain valid. Changes to the ledger format require careful consideration and documentation.

When in doubt, open an issue to discuss design before implementing larger changes.
