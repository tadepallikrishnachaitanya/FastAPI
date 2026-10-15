import logging, json, time, uuid
from logging.handlers import RotatingFileHandler
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI

app=FastAPI(title="orders-api")

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({ 
                        "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
                        "level": record.levelname,
                        "message": record.getMessage(),
                        "request_id": getattr(record, "request_id", None),
                        "route": getattr(record, "route", None),
                        "status_code": getattr(record, "status_code", None),
                        "duration_ms": getattr(record, "duration_ms", None), "service": "orders-api",
        })

logger = logging.getLogger("orders-api") # api service name to log
logger.setLevel(logging.INFO) #debug,info,warning,error, critical

file_handler = RotatingFileHandler("access.log", maxBytes=5 * 1024 * 1024, backupCount=3)
file_handler.setFormatter(JsonFormatter())
logger.addHandler(file_handler)


class AccessLogMiddleware(BaseHTTPMiddleware): #logger custom middleware
    async def dispatch(self, request, call_next):
        start = time.perf_counter()
        request.state.request_id = str(uuid.uuid4())
        response = await call_next(request)
        duration_ms = (time.perf_counter() - start) * 1000
        
        logger.info("request_completed", 
                    extra={
                        "request_id": request.state.request_id, 
                        "route": request.url.path,
                        "status_code": response.status_code, 
                        "duration_ms": round(duration_ms, 2),
            })
        response.headers["X-Request-ID"] = request.state.request_id
        return response

# IMPORTANT: Register Middleware
app.add_middleware(AccessLogMiddleware)

@app.get("/logdata")
def hello():
    return {"message": "Logged the data. Observe the access.log in the project folder"}