from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status
from typing import List, Annotated


from auth.oAuth2 import get_current_user
from database import get_async_session
from user import crud
from user.schemas import UserRead, UserBase
from auth.schemas import UserAuth

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


@router.delete(
    '/{user_id}', 
    status_code=status.HTTP_204_NO_CONTENT
    )
async def delete_user(
    user_id:int ,
    db:AsyncSession= Depends(get_async_session),
    current_user: UserAuth = Depends(get_current_user)
    ):
    actual_user = await current_user
    
    return await crud.delete_user(db,user_id, actual_user.id)