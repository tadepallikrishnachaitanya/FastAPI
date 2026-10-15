#pip install prometheus-client
from fastapi import FastAPI,Response

from prometheus_client import Counter, Histogram,generate_latest
import time

app=FastAPI()

REQUEST_COUNT=Counter("api_reqeusts_total","Total number of API requests")
REQUEST_TIME= Histogram("api_request_duration_seconds", "API request duration in seconds")

@app.get("/task")
def task():
    #db logic or complex api logic (time consuming task)
    start= time.time()
    REQUEST_COUNT.inc()
    time.sleep(0.4) #kill time as if performing expensive computation (Db logic/cpu logic)
    REQUEST_TIME.observe(time.time() - start)
    return {"message" : "completed the task........."}
    
@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), media_type="text/plain")