from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status
from typing import List, Annotated


from database import get_async_session
from user import crud
from user.schemas import UserRead, UserBase

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.get('/all',status_code=status.HTTP_200_OK, response_model=List[UserRead])
async def get_all_users(db:AsyncSession=Depends(get_async_session)):
    return await crud.get_all_users(db)



@router.post(
    '/create', 
    status_code=status.HTTP_201_CREATED,
    response_model=UserRead)
async def create_user(user:UserBase, db:AsyncSession= Depends(get_async_session)):
    return await crud.create_user(db,user)


@router.get(
    '/get', 
    status_code=status.HTTP_200_OK,
    response_model=UserRead | None)
async def get_user_by_username(username:str ,db:AsyncSession= Depends(get_async_session)):
    return await crud.get_user_by_username(db,username)