from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user_router, admin_router, moderator_router, article_router, favorite_router, auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
)

@app.get("/")
async def root():
    return {"message": "Hello Researcher!"}

app.include_router(auth_router.router, prefix="/auth", tags=["auth"])

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(admin_router.router, prefix="/admins", tags=["admins"])
app.include_router(moderator_router.router, prefix="/moderators", tags=["moderators"])

app.include_router(article_router.router, prefix="/articles", tags=["articles"])
app.include_router(favorite_router.router, prefix="/favorites", tags=["favorites"])
