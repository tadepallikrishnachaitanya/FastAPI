from prometheus_client import Counter, Histogram, generate_latest
#pip install prometheus-client
'''
Counter :  Counts events, such as number of API requests or errors.
Histogram : Measures distributions, commonly API response/request duration.
generate_latest :  Generates the metrics in Prometheus exposition format.
'''

from fastapi import FastAPI,Response
from starlette.middleware.base import BaseHTTPMiddleware
app=FastAPI()

REQUEST_COUNT = Counter("http_requests_total", "Total requests", ["method", "route", "status"]) 
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Latency", ["route"])
ERROR_COUNT = Counter("http_errors_total", "5xx/4xx errors", ["route", "status"])

class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        with REQUEST_LATENCY.labels(route=request.url.path).time(): 
            response = await call_next(request)
            REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
            if response.status_code >= 400:
                ERROR_COUNT.labels(request.url.path, response.status_code).inc() 
            return response

# IMPORTANT: Register Middleware
app.add_middleware(MetricsMiddleware)

@app.get("/metrics") 
async def metrics():
    return Response(generate_latest(), media_type="text/plain")
#localhost:8000/metrics
#localhost:8000/docs