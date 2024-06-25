from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return { "hello": "world" }

@app.get("/items/{i_id}")
def read_item( 
              i_id: int, 
              q: str, 
              name: str = None,      
              price: Optional[float] = None
              ):
    return { "i_id": i_id, "q": q, "name": name, "price": price }
