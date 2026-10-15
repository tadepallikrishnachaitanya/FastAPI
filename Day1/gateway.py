from fastapi import FastAPI

from . import router

app = FastAPI()
app.include_router(router.greet_router)