# Day 1 Notes - FastAPI Basics

## 1. Project overview
This workspace is a beginner FastAPI project focused on understanding core web API concepts, route handling, request and response models, templates, dependency injection, and the difference between synchronous and asynchronous code.

Files reviewed:
- `Day1/main.py` - main FastAPI app with routes and Pydantic models
- `Day1/async.py` - asynchronous task example using `asyncio`
- `Day1/sync.py` - blocking version using `time.sleep()`
- `Day1/templates/index.html` - simple HTML template
- `test.py` - basic Python script example
- `requirements.txt` - project dependencies

---

## 2. Setup and dependencies
The app uses FastAPI and Uvicorn:

```bash
pip install fastapi
pip install uvicorn[standard]
```

To start the server, the code comments show:

```bash
uvicorn main:app --reload
```

In this workspace, the app is inside `Day1/main.py`, so the command may also be run from that folder or by using the package-style path such as:

```bash
uvicorn Day1.main:app --reload
```

Installed dependencies include:
- `fastapi`
- `uvicorn`
- `pydantic`
- `starlette`
- `typing_extensions`

---

## 3. Creating a FastAPI app
The app is created with:

```python
from fastapi import FastAPI
app = FastAPI()
```

This object is used to register routes and handle HTTP requests.

---

## 4. Routes and endpoint basics
FastAPI routes are defined using decorators like `@app.get()`, `@app.post()`, etc.

### Example: Home route
```python
@app.get("/")
def home():
    return {"message": "FastAPI welcomes you"}
```

This creates a GET endpoint at the root URL and returns JSON.

### Example: Path parameters
```python
@app.get("/users/{id}")
async def get_user(id: int):
    return {"userId": id}
```

This captures a value from the URL and converts it to an integer using type hints.

### Example: Optional query parameter with pagination
```python
@app.get("/contacts/{cid}")
def contact_details(cid: int, page: Optional[int] = 1):
    if page:
        return {'contact_id': cid, 'page': page}
    return {'contact_id': cid}
```

This demonstrates:
- path parameter: `cid`
- query parameter: `page`
- default parameter handling

### Example: Query parameters
```python
@app.get("/search", description="Search for name Chay")
async def search(name: str, age: int):
    return {"Name": name, "Age": age}
```

This expects values like:

```text
/search?name=Chay&age=25
```

---

## 5. HTML templates with Jinja2
FastAPI can return HTML pages using templates.

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
```

And a route:

```python
@app.get("/homepage")
def web(request: Request):
    return templates.TemplateResponse(request, "index.html")
```

This is how FastAPI serves HTML pages from a `templates` folder.

The template file in the project is very simple:

```html
<h>Check</h>
```

This shows the basic idea that HTML content can be rendered and returned to the browser.

---

## 6. Pydantic models for request and response validation
Pydantic is used to define data schemas.

### Request model example
```python
class Employee(BaseModel):
    id: int
    name: str
    salary: float
```

```python
@app.post("/employee", description="Create new employee")
async def create(emp: Employee):
    return emp
```

This means FastAPI will validate incoming JSON against the `Employee` schema before passing it to the function.

### Response model example
```python
class User(BaseModel):
    id: int
    name: str

@app.get('/user', response_model=User)
def get_user():
    return User(id=1, name='Chay')
```

`response_model` tells FastAPI how to serialize the returned data and ensures the response matches the schema.

---

## 7. Dependency Injection
FastAPI supports dependency injection through the `Depends` function.

```python
def verify():
    return {"user": "Admin"}

@app.get('/dashboard')
async def dashboard(user=Depends(verify)):
    return user
```

This pattern is useful for:
- authentication
- authorization
- logging
- database access
- caching
- shared validation logic

The dependency runs before the route function executes and provides data to it.

---

## 8. Async vs sync execution
The workspace includes two example scripts to compare async and sync task execution.

### Synchronous version (`Day1/sync.py`)
```python
import time

def run_task(name, seconds):
    time.sleep(seconds)
```

This blocks the program. Each task waits one after the other, so total runtime increases:

```text
upload.. -> wait 5s
download.. -> wait 3s
backup.. -> wait 5s
```

Total time roughly equals the sum of all delays.

### Asynchronous version (`Day1/async.py`)
```python
import asyncio

async def run_task(name, seconds):
    await asyncio.sleep(seconds)
```

```python
async def main():
    await asyncio.gather(
        run_task("upload..", 5),
        run_task("download..", 3),
        run_task("backup..", 5)
    )
```

This allows multiple tasks to run concurrently without blocking each other. The program completes faster because the tasks overlap while waiting.

### Key takeaway
- `time.sleep()` blocks execution.
- `asyncio.sleep()` yields control and allows other tasks to continue.
- Async code is useful for I/O-heavy tasks such as network requests, database calls, and file operations.

---

## 9. Important FastAPI concepts learned in Day 1
- `FastAPI()` creates the app instance
- route decorators define endpoint behavior
- path parameters and query parameters are easy to declare with Python type hints
- Pydantic models validate incoming and outgoing data
- `response_model` helps with structured API responses
- `Depends` enables reusable logic and dependency injection
- Jinja templates help render HTML pages
- async programming improves efficiency for concurrent workloads

---

## 10. Summary
Day 1 focused on building a strong foundation in FastAPI. The main lessons were how to define endpoints, accept request data, validate it with Pydantic, return JSON or HTML, and use dependency injection. The project also introduced the idea that asynchronous tasks can run efficiently compared to synchronous blocking operations.

This is the basic foundation needed before moving into more advanced topics such as database integration, CRUD operations, authentication, and middleware.



===================

Day 2:

===

Day 3:
Middleware
Logginf in Fast API
Contract Versioning
Jwt Auth and Authorization
====

Logginf in Fast API
logging - debugging, prod logs - grafana - splunk

import logging
severity of msg
DEBUG,INFO,WARN,ERROR
