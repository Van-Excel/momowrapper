
from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User


async def get_user_by_identifier(db: AsyncSession, identifier: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.identifier == identifier)) 
    return result.scalars().first()