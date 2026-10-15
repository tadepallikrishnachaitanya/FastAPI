# domain specific apps / apis = split and develop/test/cicd
from fastapi.routing import APIRouter


greet_router = APIRouter()


@greet_router.get("/greet", name="greet")
def greet() -> dict[str, str]:
    return {"message": "Hello World"}
