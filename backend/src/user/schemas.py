from pydantic import BaseModel, ConfigDict, validator
from fastapi import HTTPException, status
        
class UserRead(BaseModel):
    id:int
    username:str
    email:str 
    
    model_config = ConfigDict(from_attributes=True)
    
    
    
class UserBase(BaseModel):
    username:str
    email:str 
    hashed_password:str
    
    model_config = ConfigDict(from_attributes=True)
    
    
    @validator('hashed_password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail='Password should be more than 6 symbols')
        return v