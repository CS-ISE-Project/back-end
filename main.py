import sys
print(sys.path)

from fastapi import FastAPI
from app.routers import user_router, item_router

app = FastAPI()

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(item_router.router, prefix="/items", tags=["items"])

print("APP")