import logging
from fastapi import FastAPI


app=FastAPI(title="API Logging Middleware", version="1.0.0")

logging.basicConfig(level=logging.DEBUG, filename="mylog.log", filemode="a", 
                    format="[%(asctime)s] - %(process)d - %(levelname)s - %(message)s")

@app.get("/logic")
def logic():
    logging.info("uvicorn server started")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    return {"message": "Check the mylog.log file for log messages."}