from fastapi import FastAPI
from app.routers import user_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Researcher!"}

app.include_router(user_router.router, prefix="/users", tags=["users"])