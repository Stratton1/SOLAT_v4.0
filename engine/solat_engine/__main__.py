from uvicorn import run


if __name__ == "__main__":
    run("solat_engine.api.app:app", host="127.0.0.1", port=8000, reload=False)
