from fastapi import APIRouter
from models import ProductV2


router = APIRouter(prefix="/api/v2", tags=["Products V2.0"])

products=[{ "id": 1, "product_name": "Product 1", "price": 10.0, "currency": "USD" },
          { "id": 2, "product_name": "Product 2", "price": 20.0, "currency": "USD" }]

@router.get("/products", response_model=list[ProductV2])
def get_products(): # localhost:8000/api/v2/products
    return products