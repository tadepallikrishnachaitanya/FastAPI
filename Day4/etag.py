from fastapi import FastAPI, Request, Response
import hashlib, json


app = FastAPI(title="ETag API", description="API demonstrating ETag usage", version="1.0.0")

product={ "id": 1, "name": "Product 1", "price": 10.0 }

@app.get("/product/1", tags=["ETag"])
def get_product(request: Request):
    #write db logic here to fetch data from db
    
    content = json.dumps(product, sort_keys=True).encode("utf-8")
    #generate etag using md5 hash of the content
    etag = hashlib.md5(content).hexdigest()
    
    #check if the client has sent the If-None-Match header with the etag value
    client_etag = request.headers.get("If-None-Match")
    if client_etag == etag:
        return Response(status_code=304, headers={"ETag": etag})
    
    return Response(content=content, media_type="application/json", headers={"ETag": etag})