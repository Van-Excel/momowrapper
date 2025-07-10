import uuid
from app.models.wallet import Wallet
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import SessionLocal, get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserOut, TokenResponse
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", )



@router.post(
    "/register",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    responses={
        400: {"description": "Email already registered"},
        201: {"description": "User registered successfully"},
    },
)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Register a new user by email and password.

    - **email**: must be unique
    - **password**: will be securely hashed
    - Returns: `identifier`, `email`
    """
    result = await db.execute(select(User).where(User.email == user.email))
    if result.scalar():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    await db.flush()  # get new_user.id before committing

    new_wallet = Wallet(
        user_id=new_user.id,
        balance=0.00,
        currency="GHS"
    )
    db.add(new_wallet)
    await db.commit()
    await db.refresh(new_user)
    return new_user


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Authenticate user and return JWT",
    responses={
        200: {"description": "Login successful"},
        401: {"description": "Invalid credentials"},
    },
)
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    """
    Login with email and password.

    - **email**: must be registered
    - **password**: will be verified
    - Returns: `access_token`, `token_type`
    """
    result = await db.execute(select(User).where(User.email == user.email))
    db_user = result.scalar()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.identifier})
    return {"access_token": token, "token_type": "bearer"}
