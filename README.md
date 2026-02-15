# SOLAT_v4.0

IG-only auto-trading workstation with a local Python engine and a Tauri + React desktop UI using Plotly charts.

## Status
- Current phase: **Phase 0 (bootstrap + contracts-first)**
- Stop-gate policy: see `docs/STOP_POINTS.md`

## Monorepo Layout
- `engine/` Python engine (FastAPI + WS + IG adapters + backtest/sweep/exec)
- `apps/desktop/` Tauri + React desktop UI
- `shared/contracts/` optional shared schema/type artifacts
- `docs/` canonical project docs

## Canonical Docs
- `docs/PROJECT_MEMORY.md`
- `docs/BUILD_LOG.md`
- `docs/ARCHITECTURE.md`
- `docs/RUNBOOK.md`
- `docs/STOP_POINTS.md`

## Development
```bash
pnpm -w install
cd engine && uv sync
```

## Notes
- Broker scope is IG only in v4.0.
- Plotly is the only charting stack for UI; TradingView and lightweight-charts are disallowed.
