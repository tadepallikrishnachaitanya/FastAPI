#custom middleware - Metrics =profiling
import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        #write logic before request
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f"Request : {request.url.path} processed in : {process_time:.4f}secs") # localhost:8000/customers/101
        response.headers["X-Process-Time"] = str(process_time)
        return response
    
app.add_middleware(TimerMiddleware)

@app.get('/profile', tags=["Profiling endpoint"])
async def profile():
    for _ in range(100):
        pass
    return {"message":"Profiler using custom middleware. check console for profiling time and response header for X-Process-Time"}