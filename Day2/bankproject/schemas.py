from pydantic import BaseModel, ConfigDict


class CustomerIn(BaseModel):
    name: str
    email: str
    phone: str
    account_type: str
    balance: float


class CustomerOut(CustomerIn):
    id: int
    model_config = ConfigDict(from_attributes=True)
