from fastapi import FastAPI


app = FastAPI(title="SOLAT Engine", version="0.1.0-phase0")


@app.get("/api/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok", "phase": "phase0"}
