# Database models for SQLAlchemy
from sqlalchemy import Column, Float, Integer, String
from database import Base


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    account_type = Column(String(20), nullable=False)
    balance = Column(Float, default=0.0)
    