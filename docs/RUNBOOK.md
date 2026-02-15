# SOLAT_v4.0 Runbook

Last updated: 2026-02-15T04:48:41Z

## Current Phase
Phase 0 bootstrap complete. Core runtime features are not implemented yet.

## Prerequisites
- Python 3.12+
- `uv`
- Node.js 20+
- `pnpm` 9+
- Rust toolchain (for Tauri desktop build)

## Repository Setup
```bash
pnpm -w install
cd engine && uv sync
```

## Git Publish
```bash
git add -A
git commit -m "Phase 0 bootstrap: scaffold SOLAT_v4.0 monorepo and contracts"
git push -u origin main
```

## Agent Rules
- In VS Code/Codex, keep both `AGENTS.md` and `.cursorrules` present and current.
- Use `AGENTS.md` for workflow/process instructions and `.cursorrules` for concise enforcement rules.

## Engine (Planned Commands)
```bash
cd engine
uv run python -m solat_engine
uv run python -m pytest
```
Current implementation note:
- `uv run python -m solat_engine` starts a placeholder FastAPI app with `/api/v1/health`.

## Desktop UI (Planned Commands)
```bash
pnpm --filter solat-desktop dev
pnpm --filter solat-desktop build
pnpm --filter solat-desktop tauri dev
```
Current implementation note:
- Desktop app currently renders a Phase 0 scaffold view.

## Smoke Test (Phase 1 target)
```bash
cd engine
uv run python -m solat_engine.tools.ig_smoketest
```

## Troubleshooting
- If `pnpm` workspace fails, verify `pnpm-workspace.yaml` includes `apps/*`.
- If `uv sync` fails, verify Python version and lockfile state.
- If Tauri build fails, verify Rust toolchain and platform prerequisites.
- If IG connectivity fails in future phases, verify `engine/configs/ig_accounts.json` formatting and environment (`demo` vs `live`).

## Operational Safety
- Default execution mode target for first live engine tests is `DEMO_IG` only.
- Use `/execution/arm` and `/execution/disarm` controls explicitly.
- Keep kill-switch tested and reachable before any live execution mode is enabled.
