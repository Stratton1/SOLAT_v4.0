# SOLAT_v4.0 Stop Points

Last updated: 2026-02-15T04:47:45Z

Required approval gates:

## STOP POINT #0
Phase 0 bootstrap complete:
- repo scaffolding present
- canonical docs created
- contracts documented
- `.cursorrules` enforcing project hygiene

## STOP POINT #1
IG integration smoke test complete:
- IG login + candle fetch + Lightstreamer quote stream works
- multi-key pool tests pass

## STOP POINT #2
Data layer complete:
- normalized bars/quotes endpoints returning expected payloads
- WS stream events active for quotes and bar updates

## STOP POINT #3
Backtest/sweep/reporting complete:
- deterministic backtests run
- sweep runner produces canonical `report.md`, `results.csv`, `summary.json`

## STOP POINT #4
Strategies/variants/bots compile and backtest:
- strategy registry and presets available
- bot definition lifecycle functional

## STOP POINT #5
Demo auto-trader execution complete:
- `DEMO_IG` end-to-end order placement with risk rails
- reconciliation and kill-switch verified

## STOP POINT #6
Desktop UI workstation complete:
- live WS charting with Plotly
- control panel + bots + sweep/report pages integrated
- demo trade events visible on chart

## Policy
No phase may begin before explicit user approval at prior stop point.
