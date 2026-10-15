from fastapi import APIRouter
from models import ProductV1


router = APIRouter(prefix="/api/v1", tags=["Products V1.0 - Deprecated"])

products=[{ "id": 1, "name": "Product 1", "price": 10.0 },
          { "id": 2, "name": "Product 2", "price": 20.0 }]

@router.get("/products", response_model=list[ProductV1])
def get_products(): # localhost:8000/api/v1/products
    return products