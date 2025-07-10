

async def get_current_user(db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        identifier: str = payload.get("sub")  # ✅ changed
        if identifier is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await get_user_by_identifier(db, identifier)  # ✅ changed
    if user is None:
        raise credentials_exception
    return user
