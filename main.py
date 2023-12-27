from fastapi import FastAPI
from app.routers import user_router , admin_router
from fastapi.middleware.cors import CORSMiddleware
from app.routers import elasticsearch_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Researcher!"}

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(elasticsearch_router.router, prefix="/elasticsearch", tags=["elasticsearch"])
app.include_router(admin_router.router, prefix="/admins", tags=["admins"])
