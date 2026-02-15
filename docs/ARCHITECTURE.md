# SOLAT_v4.0 Architecture (Canonical)

Last updated: 2026-02-15T04:47:02Z
Contract version: `v0.1.0-phase0`

## 1) System Overview
SOLAT_v4.0 is a local desktop trading workstation with three top-level domains:
- `engine` (Python/FastAPI): IG integration, market/account data normalization, backtest/sweep, execution/risk control.
- `apps/desktop` (Tauri + React + TypeScript): operator UI with live controls and Plotly charts.
- `shared` (optional): shared contract artifacts/types and schema metadata.

Primary runtime flow:
1. Engine authenticates with IG REST and starts Lightstreamer subscriptions.
2. Engine normalizes quotes, bars, account, order and bot status into internal models.
3. UI pulls snapshots via REST and subscribes to engine WS topics for live updates.
4. Backtest/sweep pipelines run over stored bars and emit deterministic artifacts.

## 2) Repository Layout
- `engine/`
- `apps/desktop/`
- `shared/contracts/`
- `docs/`

## 3) Canonical Data Models
All timestamps are UTC ISO-8601 with milliseconds unless stated otherwise.

### QuoteTick
```json
{
  "symbol": "string",
  "bid": 0.0,
  "ask": 0.0,
  "last": 0.0,
  "ts": "2026-02-15T04:37:11.000Z"
}
```
Notes:
- `last` is optional and may be null when unavailable from IG feed.

### Bar
```json
{
  "symbol": "string",
  "timeframe": "M1|M5|M15|H1|H4|D1",
  "ts_open": "2026-02-15T04:35:00.000Z",
  "ts_close": "2026-02-15T04:39:59.999Z",
  "o": 0.0,
  "h": 0.0,
  "l": 0.0,
  "c": 0.0,
  "volume": 0.0,
  "source": "IG_REST|IG_STREAM|DERIVED",
  "quality": "OK|PARTIAL|GAP_FILLED|ESTIMATED"
}
```

### AccountSnapshot
```json
{
  "balance": 0.0,
  "equity": 0.0,
  "margin_used": 0.0,
  "margin_avail": 0.0,
  "positions": [],
  "orders": [],
  "ts": "2026-02-15T04:37:11.000Z"
}
```

### OrderIntent
```json
{
  "symbol": "string",
  "direction": "BUY|SELL",
  "size": 0.0,
  "order_type": "MARKET|LIMIT|STOP",
  "entry_price": 0.0,
  "stop_loss": 0.0,
  "take_profit": 0.0,
  "time_in_force": "GTC|DAY|IOC|FOK",
  "strategy_ref": "string",
  "bot_id": "string",
  "tags": ["string"],
  "ts": "2026-02-15T04:37:11.000Z"
}
```

### OrderResult
```json
{
  "order_id": "string",
  "status": "ACCEPTED|REJECTED|FILLED|PARTIAL|CANCELLED",
  "reason": "string",
  "filled_size": 0.0,
  "avg_fill_price": 0.0,
  "broker_ref": "string",
  "ts": "2026-02-15T04:37:11.000Z"
}
```

### SignalIntent
```json
{
  "symbol": "string",
  "tf": "M1|M5|M15|H1|H4|D1",
  "direction": "LONG|SHORT|FLAT",
  "entry_price": 0.0,
  "stop_loss": 0.0,
  "take_profit": 0.0,
  "confidence": 0.0,
  "tags": ["string"],
  "reason": "string",
  "entry_ts": "2026-02-15T04:37:11.000Z",
  "ts": "2026-02-15T04:37:11.000Z"
}
```
Notes:
- `entry_ts`, `entry_price`, `stop_loss`, `take_profit`, `direction`, `confidence`, `tags`, `reason` are required for chart overlays and hover details.

### BotDefinition
```json
{
  "bot_id": "string",
  "strategy_id": "string",
  "variant_id": "string",
  "symbol": "string",
  "tf": "M1|M5|M15|H1|H4|D1",
  "risk_config": {
    "risk_per_trade_pct": 0.0,
    "max_concurrent_risk_pct": 0.0,
    "max_open_positions": 0
  },
  "execution_mode": "DEMO_SIM|DEMO_IG|LIVE_IG",
  "enabled": false
}
```

## 4) Engine Contract (REST)
Base URL (planned): `/api/v1`

### GET `/health`
- Returns engine status, uptime, version, broker connectivity.

### GET `/symbols`
- Returns IG-only symbol catalog (epics mapped to display symbols).

### GET `/quotes`
- Returns last normalized quotes snapshot for subscribed symbols.

### GET `/bars?symbol&tf&limit`
- Returns last `N` bars + optional forming bar when present.

### GET `/data/available-range?symbol&tf`
- Returns data coverage metadata:
  - `first_ts`, `last_ts`, `missing_bar_pct`, `gap_count`, `bar_count`

### POST `/backtest/run`
- Starts backtest job from stored bars.
- Returns `run_id` and initial status.

### POST `/sweep/run`
- Starts grid sweep job.
- Returns `sweep_id` and queued config summary.

### GET `/sweep/:id/report`
- Returns canonical report artifacts in `md|csv|json` format.

### GET `/bots`
- Returns bot definitions and runtime status.

### POST `/bots`
- Creates or updates bot definition.

### POST `/bots/:id/start`
- Arms and starts a bot subject to risk gates.

### POST `/bots/:id/stop`
- Stops bot and disarms execution for that bot.

### POST `/execution/place-order`
- Accepts `OrderIntent`, applies safety checks, routes to selected execution mode.

### POST `/execution/arm`
- Arms execution globally (precondition for live order placement).

### POST `/execution/disarm`
- Disarms execution globally (reject new order intents).

### POST `/execution/kill-switch`
- Emergency stop: disarm + cancel pending orders + stop managed bots.

## 5) Engine Contract (WebSocket Topics)
Transport: engine WS endpoint with topic subscription payloads.

Topics:
- `quotes` (live quote ticks/updates)
- `bar_updates` (forming + closed bar events)
- `orders` (order lifecycle updates)
- `positions` (position lifecycle updates)
- `bot_status` (bot state transitions)
- `sweep_progress` (job progress + completion)

## 6) Module Boundaries
Engine planned modules:
- `solat_engine/brokers/ig/` for IG adapters and auth/pooling/rate controls.
- `solat_engine/data/` for quote/bar normalization and storage.
- `solat_engine/backtest/` for deterministic test runner.
- `solat_engine/sweep/` for parallel grid sweeps + report emission.
- `solat_engine/execution/` for routing, risk checks, reconciliation.
- `solat_engine/api/` for FastAPI routes + WS hub.

Desktop planned modules:
- `src/pages/*` for workstation pages.
- `src/features/chart/*` for Plotly chart lifecycle, overlays, drawings.
- `src/features/bots/*`, `src/features/backtests/*`, `src/features/sweeps/*`.
- `src/lib/ws` + `src/lib/api` for engine transport adapters.

## 7) Persistence Strategy (Planned)
- SQLite: metadata/state snapshots, bot configs, app settings.
- Parquet: OHLCV bars and run outputs (backtests/sweeps).
- Optional DuckDB: query acceleration over parquet datasets.

## 8) Contract Governance
- Any endpoint/schema changes must be made here before implementation.
- `docs/ARCHITECTURE.md` is the source of truth for contracts in Phase 0.
- Future: generate OpenAPI + TS types into `shared/contracts` from engine models.
- Agent governance in this repo is enforced by `AGENTS.md` and `.cursorrules`; these are operational rules, while this document remains the technical contract source of truth.

## 9) Phase 0 Implementation Notes
- Implemented scaffold endpoint: `GET /api/v1/health` in `engine/solat_engine/api/app.py`.
- Remaining REST/WS surfaces in Section 4 and Section 5 are contract-defined and scheduled for implementation in later phases.
