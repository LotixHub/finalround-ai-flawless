from fastapi import FastAPI

app = FastAPI(title="FinalRound AI")

@app.get("/")
def root():
    return {"message": "ok"}
    