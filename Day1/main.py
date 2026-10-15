from typing import Optional

from fastapi import Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#endpoints
@app.get("/")
def home():
    return {"message":"FastAPI welcomes you"}

@app.get("/homepage")
def web(request: Request):
    return templates.TemplateResponse(request,"index.html")


@app.get("/users/{id}")
async def get_user(id:int):
    #connect to fb and get user and return data
    return {"userId":id}


@app.get("/contacts/{cid}")
def contact_details(cid:int, page:Optional[int]=1):
    #logic of pagination
    if page:
        return {'contact_id':cid,'page':page}
    return {'contact_id':cid}

#query parameters
@app.get("/search", description="Search for name Chay")
async def search(name:str, age:int):
    #write a logic
    return {"Name":name, "Age":age}

# pydantic model (request and response)
#model map db table - ORM - request and response
class Employee(BaseModel):
    id:int
    name:str
    salary:float
    
@app.post("/employee", description="Create new employee")
async def create(emp : Employee): #http request model
    #store in Db
    return emp

#response model - json serializer
class User(BaseModel):
    id:int
    name:str
    
@app.get('/user', response_model=User)
def get_user():
    return User(id=1,name='Chay')

#---------
# Dependency Injection (Authentication/ authorization/logger/db call/ cache)

def verify():
    return {"user":'Admin'}

@app.get('/dashboard')
async def dashboard(user=Depends(verify)):
    return user


# request middleware - response middleware
@app.middleware('http') # http interceptor
async def log_request(request:Request, call_next):
    print(f"Request URL : {request.url}")
    print(f"Request Method : {request.method}")
    response=await call_next(request)
    print(f"Response Status Code : {response.status_code}")
    return response

