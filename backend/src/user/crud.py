from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from user.models import User
from user.schemas import UserBase

from hash.hash import Hash



async def get_all_users(db:AsyncSession):
    query = select(User)
    res =  await db.execute(query)
    users = res.scalars().all()
    return users


async def create_user(db:AsyncSession, user:UserBase):
    try:
        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=Hash.bcrypt(user.hashed_password)
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='user or email already exist')
    
    
    
    
async def get_user_by_username(db:AsyncSession, username:str):
    query = select(User).where(User.username == username)
    res = await db.execute(query)
    user = res.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
        
    return user


async def delete_user(db:AsyncSession, user_id:int, current_user_id:int):
    query = select(User).where(User.id == user_id)
    res = await db.execute(query)
    user = res.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
        
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Only owner can delete own account'
        )
    await db.delete(user)
    await db.commit()
    return 'deleted'

