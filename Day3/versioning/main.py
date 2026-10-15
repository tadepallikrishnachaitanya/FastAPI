from fastapi import FastAPI
from routers.v1 import router as v1_router
from routers.v2 import router as v2_router

app = FastAPI(title="Product API", description="API for managing products", version="2.0.0")

app.include_router(v1_router, deprecated=True)  # Marking v1 as deprecated
app.include_router(v2_router)

@app.get("/", tags=["Products API"])
def home():
    return {"message": "Welcome to the Products Versioning.",
            "versions": ["DeprecationWarning: The v1 API is deprecated and will be removed in future releases. Please migrate to v2."]
            }
