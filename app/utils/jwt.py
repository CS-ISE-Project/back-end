from app.config.creds import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM

from fastapi import HTTPException , status
from jose import JWTError, jwt

from typing import List, Union
from datetime import datetime, timedelta

def create_access_token(data: dict, role: str, expires_delta: timedelta = None):
    to_encode = data.copy()
    to_encode["role"] = role
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None  
    
def verify_token(token: str, role: Union[str, List[str]] ) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if isinstance(role,str) : 
            if payload.get('role') != role:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Operation not permitted",
                    headers={"WWW-Authenticate": "Bearer"},
                )
                
        if isinstance(role,list) :
            if payload.get('role') not in role : 
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Operation not permitted",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
            
        return True
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
              
def verify_session(token : str , id : str) -> bool : 
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        if payload.get('id') != id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operation not permitted",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return True 
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
