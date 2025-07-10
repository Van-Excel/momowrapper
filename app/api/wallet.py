from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import SessionLocal
from app.models.user import User
from app.models.wallet import Wallet
from app.schemas.wallet import WalletOut
from app.core.security import get_current_user

from app.crud.user import get_user_by_identifier

router = APIRouter(prefix="/wallet", tags=["Wallet"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/me", response_model=WalletOut, summary="Get current user's wallet")
async def get_wallet_me(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get wallet information for the authenticated user.
    """
    result = await db.execute(select(Wallet).where(Wallet.user_id == current_user.id))
    wallet = result.scalar_one_or_none()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet


@router.post("/wallets/{user_identifier}", response_model=WalletOut)
async def create_wallet_for_user(user_identifier: str, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_identifier(db, user_identifier)  # ✅ using identifier
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    existing = await db.execute(select(Wallet).where(Wallet.user_id == user.id))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Wallet already exists")

    wallet = Wallet(user_id=user.id)
    db.add(wallet)
    await db.commit()
    await db.refresh(wallet)
    return wallet
