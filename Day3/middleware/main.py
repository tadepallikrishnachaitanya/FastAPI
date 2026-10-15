#middleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200","http://localhost:3000"], # Allow only these origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow only these methods
    allow_headers=["*"],
)


app.add_middleware(HTTPSRedirectMiddleware) #http://localhost:8000 -> https://localhost:8000
app.add_middleware(GZipMiddleware, minimum_size=1000) #compress response if size > 1000 bytes

@app.get("/")
def home():
    return {"message": "FastAPI with Middleware!"}