from pydantic import BaseModel, ConfigDict

        
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