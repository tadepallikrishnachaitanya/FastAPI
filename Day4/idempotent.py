from fastapi import FastAPI, Header
import uuid

app =FastAPI(title="Idempotent API", description="API demonstrating idempotent operations", version="1.0.0")

orders = []
processed = {} # db data structure to store processed payments with idempotency keys
@app.post("/orders", tags=["non-idempotent"])
def create_order(order: dict):
    orders.append(order)
    return {"message": "Order created successfully", "count": len(orders)}

@app.post("/payments", tags=["idempotent handled"])
def process_payment(amount: int, idempotency_key: str = Header(...)):
    if idempotency_key in processed:
        return {"message": "Payment already processed", "payment": processed[idempotency_key]}
    
    payment={ "payment id": str(uuid.uuid4()),
             "amount": amount,
             "status": "processed" }
    
    processed[idempotency_key] = payment
    return {"message": "Payment processed successfully", "payment": payment}