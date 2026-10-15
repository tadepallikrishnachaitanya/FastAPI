from typing import List

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from .models import Employee

emps_db: List[Employee] = [] #mocked data

tags_metadata = [
    {
        "name": "Employees",
        "description": "Operations related to employees."
    }
]

app = FastAPI(
    title="Bank API", 
    version="1.0.0",
    openapi_tags=tags_metadata)


@app.exception_handler(Exception)
async def global_exception_handler(_request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "BOFA: An unexpected error occurred.", "details": str(exc)},
    )
    
@app.get("/globalerror", tags=["Testing Global Error"])
async def trigger_global_error():
    raise Exception("This is a test exception for global error handling.")


#CRUD - Post, get, put, delete (http verbs)
@app.get("/employees", response_model=List[Employee], tags=["Get Employees"])
def get_employees():
    #talk to db
    return emps_db


@app.post("/employees", response_model=Employee, tags=["Create Employee"])
def create_employee(employee: Employee):
    for emp in emps_db:
        if emp.id == employee.id:
            raise HTTPException(status_code=409, detail="Employee with this ID already exists.")
    emps_db.append(employee)
    return employee

# Please complete put- update
@app.put("/employees/{employee_id}", response_model=Employee, tags=["Update Employee"])
def update_employee(employee_id: int, employee: Employee):
    for i, emp in enumerate(emps_db):
        if emp.id == employee_id:
            emps_db[i] = employee
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{employee_id}", tags=["Delete Employee"])
def delete_employee(employee_id: int):
    for i, emp in enumerate(emps_db):
        if emp.id == employee_id:
            emps_db.pop(i)
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")
