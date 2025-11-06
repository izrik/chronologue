from fastapi import FastAPI

app = FastAPI(title="Chronologue API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Chronologue Time Tracker API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}