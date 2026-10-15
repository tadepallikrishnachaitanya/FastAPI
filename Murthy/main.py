# https://survey.zohopublic.com/zs/s7DF0I




# pip install fastapi 
#pip install uvicorn[standard]

from typing import Optional
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates


app=FastAPI()
templates=Jinja2Templates(directory="templates")

#endpoints
@app.get("/")
def home():
    return {"message":"Fast API welcomes you"}

@app.get("/homepage")
def web(request: Request):
    return templates.TemplateResponse(request,"index.html")

#route parameters
@app.get("/users/{id}")   #localhost:8000/users/101
async def get_user(id:int):
    #connect to db and get user and return data
    #result=await dbcall(id)
    return {"userId":id}

#optional params
@app.get("/contacts/{cid}")
def contact_details(cid:int, page:Optional[int]=1):
    #logic for pagination
    if page:
        return {'contact_id':cid,'page':page}
    return {'contact_id': cid}

#query params
@app.get("/search",description="Search for name Murthy")
async def search(name:str, age:int):
    #write the logic
    return {"Name": name, "Age":age} #json serialized    import jsonify

#pydantic model (request and response)
from pydantic import BaseModel
#model - request and response
class Employee(BaseModel):
    id:int
    name:str
    salary: float

@app.post("/employee",description="Create new employee")
async def create(emp : Employee):#http request model
    #store emp in db
    return emp

#response model - json serializer
class User(BaseModel):
    id:int
    name:str

@app.get('/user', response_model=User)
def get_user():
    return User(id=1,name='Murthy')
#-----------------------------------------
#Dependency Injection  (authentication/ authorization/ logger/db call/cache)
def verify():
    return {"user":'Admin'}

from fastapi import Depends
@app.get('/dashboard')
async def dashboard(user=Depends(verify)):
    return user

#request middleware and response middleware

@app.middleware('http')   #http interceptor
async def timer(request: Request,call_next):
    print("Profiling : Before request")
    response= await call_next(request)
    print("After request")
    return response
    
