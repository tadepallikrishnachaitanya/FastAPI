from fastapi import FastAPI
from pydantic import BaseModel
from logic import checker

app=FastAPI()

class Applicant(BaseModel):
    income: float
    age : int
    type : str
    
@app.post('/loan-eligibility')
def check_eligibility(applicant : Applicant ):
    result=checker(income=applicant.income,
                              age=applicant.age,
                              employee_type=applicant.type)
    return {'eligbility':result}