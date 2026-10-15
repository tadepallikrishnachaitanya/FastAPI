# entrypoint
from schemas import CustomerIn
from fastapi import FastAPI  # type: ignore[import-not-found]

from database import Base, engine, sessionmaker
import crud
from schemas import CustomerOut

# create db and tables and session
Base.metadata.create_all(bind=engine)  # code first approach - create tables from models

app = FastAPI(title="Bank Customer API", version="1.0.0")


@app.get("/customers", tags=["Get Customers"], response_model=list[CustomerOut])
def get_customers():
    db = sessionmaker()
    try:
        return crud.all(db)
    finally:
        db.close()
        
@app.get("/customers/{customer_id}", tags=["Get Customer"], response_model=CustomerOut)
def get_customer(customer_id: int):
    db = sessionmaker()
    try:
        return crud.get(db, customer_id)
    finally:
        db.close()
        
@app.post("/customers", tags=["Create Customer"], response_model=CustomerOut)
def create_customer(customer: CustomerOut):
    db = sessionmaker()
    try:
        return crud.create(db, customer)
    finally:
        db.close()

@app.put("/customers/{customer_id}", tags=["Update Customer"], response_model=CustomerOut)
def update_customer(customer_id: int, customer: CustomerIn):
    db = sessionmaker()
    try:
        return crud.update(db, customer_id, customer)
    finally:
        db.close()
        
@app.delete("/customers/{customer_id}", tags=["Delete Customer"], response_model=CustomerOut)
def delete_customer(customer_id: int):
    db = sessionmaker()
    try:
        return crud.delete(db, customer_id)
    finally:
        db.close()
