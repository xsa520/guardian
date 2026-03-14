# Contributing to Guardian

Thank you for your interest in contributing. This document covers how to open issues, submit changes, and align with Guardian's development principles.

## Opening Issues

- Use the GitHub issue tracker for bugs, feature requests, and design discussions.
- For bugs: include steps to reproduce, expected vs actual behavior, and environment (OS, Python version).
- For features: describe the use case and how it fits Guardian's governance model (intent, policy, decision, evidence).
- Check existing issues and discussions before opening a duplicate.

## Pull Request Guidelines

- Open a pull request from a branch (e.g. `feature/your-change` or `fix/issue-description`).
- Keep changes focused. One PR should address one logical change.
- Ensure tests pass: run `pytest tests/` from the repository root.
- Ensure examples still run: `python examples/demo.py`, `python examples/replay_demo.py`, `python examples/agent_integration_demo.py`.
- Update documentation (README, ARCHITECTURE, or code comments) if behavior or APIs change.
- PR titles and descriptions should clearly state what is being changed and why.

## Development Principles

Guardian is governance infrastructure for AI agents. Contributions should align with these principles:

- **Deterministic decisions** — The decision path must remain deterministic for a given intent and policy. Avoid introducing non-determinism in the Policy Engine, Decision Engine, or Permission Model.
- **Policy as code** — New behavior should be expressible via policy rules where possible, rather than new hardcoded branches. Extend the policy schema or loader instead of special-casing in code when feasible.
- **Replay verification** — Evidence ledger format and hash chain semantics must stay consistent so that replay and ledger validation remain valid. Changes to the ledger format require careful consideration and documentation.

When in doubt, open an issue to discuss design before implementing larger changes.
