from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user_router, admin_router, moderator_router, article_router, favorite_router, auth_router, search_router, upload_router, moderation_router, modifications_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_headers=["*"],
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
app.include_router(search_router.router, prefix="/search", tags=["search"])
app.include_router(favorite_router.router, prefix="/favorites", tags=["favorites"])

app.include_router(modifications_router.router, prefix="/modifications", tags=["modifications"])
app.include_router(moderation_router.router, prefix="/moderation", tags=["moderation"])

app.include_router(upload_router.router, prefix="/upload", tags=["upload"])