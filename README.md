## Python fastAPI

1. Installation

```sh
    pip install fastapi uvicorn
```
2. Create a simple fastapi, in the project-folder, in main.py incude the
   following code

```py
# ./project-folder/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

```
3. Run the app

    `uvicorn main:app --reload`

4. Access the app

```
     Swagger UI: http://127.0.0.1:8000
     ReDoc:      http://127.0.0.1:8000/items/1?q=somequery
```
5. API Documentation

```
   http://127.0.0.1:8000/docs
   http://127.0.0.1:8000/redoc
```
