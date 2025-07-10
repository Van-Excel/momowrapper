from app.core.config import settings

from fastapi import FastAPI
from app.api import auth, wallet
from app.db.base import Base
from app.db.session import engine

app = FastAPI()

print(settings.DATABASE_URL)

app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(wallet.router)

# Optional: Create tables on startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
