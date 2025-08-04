from fastapi import FastAPI
from router.users import router

app = FastAPI()
app.include_router(router)

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
