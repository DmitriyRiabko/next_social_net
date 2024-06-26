from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from database import get_async_session
from user import crud
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
 
 # openssl rand -hex 32
SECRET_KEY = 'df53e1ac62c55b95f2c4e8eff42fa3b20f8b1317fae9d83715c14f2529bd5042'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 120

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt
 
def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_async_session)
):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("username")
    if username is None:
      raise credentials_exception
  except JWTError:
    raise credentials_exception
  user = crud.get_user_by_username(db, username=username)
  if user is None:
    raise credentials_exception
  return user