from typing import Optional

from sqlalchemy.orm import Session

from models import Customer
from schemas import CustomerIn


def create(db: Session, data: CustomerIn) -> Customer:
    customer = Customer(**data.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def all(db: Session) -> list[Customer]:
    return db.query(Customer).all()


def get(db: Session, customer_id: int) -> Optional[Customer]:
    return db.query(Customer).filter(Customer.id == customer_id).first()


def update(db: Session, customer_id: int, data: CustomerIn) -> Optional[Customer]:
    customer = get(db, customer_id)
    if customer:
        customer.name = data.name
        customer.email = data.email
        customer.balance = data.balance
        db.commit()
        db.refresh(customer)
    return customer


def delete(db: Session, customer_id: int) -> Optional[Customer]:
    customer = get(db, customer_id)
    if customer:
        db.delete(customer)
        db.commit()
    return customer