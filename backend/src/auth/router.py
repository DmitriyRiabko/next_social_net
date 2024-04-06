from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from sqlalchemy import select


from database import get_async_session
from user.models import User
from hash.hash import Hash
from .oAuth2 import create_access_token


router = APIRouter(tags=["auth"])


@router.post("/login",status_code=status.HTTP_202_ACCEPTED)
async def login(
    request: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_async_session)
):
    stmt = select(User).where(User.username == request.username)
    res = await db.execute(stmt)
    user = res.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )

    if not Hash.verify(user.hashed_password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password"
        )

    access_token = create_access_token(data={"username": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.username,
    }