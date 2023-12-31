from fastapi import FastAPI
from app.routers import user_router , admin_router , moderator_router , article_router , auth_router
from fastapi.middleware.cors import CORSMiddleware
from app.routers import elasticsearch_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Researcher!"}

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(elasticsearch_router.router, prefix="/elasticsearch", tags=["elasticsearch"])
app.include_router(admin_router.router, prefix="/admins", tags=["admins"])
app.include_router(moderator_router.router, prefix="/moderators", tags=["moderators"])
app.include_router(article_router.router, prefix="/articles", tags=["articles"])


app.include_router(auth_router.router, prefix="/auth", tags=["auth"])
