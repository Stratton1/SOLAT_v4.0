# SOLAT_v4.0 Project Memory

Last updated: 2026-02-15T04:47:45Z

## Scope
SOLAT_v4.0 is an IG-only local desktop trading platform with:
- Python engine (`/engine`) for IG REST + Lightstreamer integration, data normalization, backtest/sweep, and auto-trading.
- Tauri + React desktop UI (`/apps/desktop`) using Plotly (no TradingView).

## Decisions (Canonical)
- Broker scope for v4.0 is IG only.
- UI charting is Plotly (`plotly.js-finance-dist` + `react-plotly.js`) only.
- Repo style is monorepo with `engine`, `apps/desktop`, and optional `shared` contracts.
- Engine API-first contract is defined in `docs/ARCHITECTURE.md`.
- Phase gates are mandatory and tracked in `docs/STOP_POINTS.md`.
- Codex/VS Code governance should remain explicit through repo rules files (`AGENTS.md` + `.cursorrules`) so agent behavior is deterministic across sessions.
- Tooling baseline:
  - Python dependency manager/runtime: `uv`
  - Frontend/package manager: `pnpm`
  - Desktop shell: Tauri
- Initial UI state management choice: `zustand` (minimal store approach).

## Invariants
- No TradingView or `lightweight-charts` dependencies.
- All schema/endpoint changes must be documented before implementation.
- Every code change must have a corresponding `docs/BUILD_LOG.md` entry.
- Stop for user approval at each stop point before advancing phases.
- Canonical docs that must remain current: `PROJECT_MEMORY`, `BUILD_LOG`, `ARCHITECTURE`, `RUNBOOK`, `STOP_POINTS`.

## Current State
- Phase 0 scaffolding complete.
- Git repository initialized at `/Users/joseph/Projects/SOLAT_ALL/solat_v4.0`.
- GitHub repository created: `https://github.com/Stratton1/SOLAT_v4.0`.
- Initial commit pushed to `origin/main` at `d1e65cddb07f47450d764114708c3432d378ab4f`.
- Root governance/tooling files added (`.cursorrules`, `.editorconfig`, `.gitignore`, workspace configs).
- Canonical docs created and populated with contracts and run instructions.
- Engine placeholder package and health route scaffolded.
- Desktop (Tauri + React) skeleton scaffolded.

## Active TODOs
- STOP POINT #0 approval required before Phase 1.
- Phase 1 target: implement IG REST/Lightstreamer broker modules with credential pools and rate-limit failover tests.
- Add `solat_engine.tools.ig_smoketest` CLI for IG connectivity smoke test.
