#DAL 
#pip install pyjwt  bcrypt email-validator

from datetime import datetime,timedelta, timezone
import jwt
import bcrypt #store hash pwd in db

SECRET_KEY= "change-this-secret-key-in-production-murthy"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

#hash the pwd and write it in db for security
def hash_password(password:str) ->str :
    password_bytes= password.encode("utf-8")[:70] #string must be converted to bytes before bcrypt
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")
    
#pwd verification
def verify_password(password:str, hashed_password:str) -> bool :
    password_bytes=password.encode("utf-8")[:70]
    return bcrypt.checkpw(password_bytes,hashed_password.encode("utf-8"))

#create jwt token
def create_access_token(username : str) -> str :
    expire=datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload={"sub":username, "exp":expire}
    return jwt.encode(payload,SECRET_KEY,ALGORITHM)#xxxx.yyyyyy.zzzzzzz
    

def decode_access_token(token:str): #validate
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])