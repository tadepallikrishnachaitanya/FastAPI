from typing import Optional

from pydantic import BaseModel, Field, StrictInt, StrictStr

class Employee(BaseModel):
    id: StrictInt = Field(..., gt=0, title="Employee ID")
    name: StrictStr = Field(..., min_length=3, max_length=25)
    department: str = Field(..., min_length=3, max_length=20)
    age: Optional[StrictInt] = Field(default=None, ge=18, le=65)