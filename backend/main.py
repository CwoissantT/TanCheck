from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data model like a request body in Express
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

# GET route
@app.get("/status")
async def get_status():
    return {"message": "Server is up and running"}

# POST route - handling JSON body
@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    # Here you can add logic to save to DB etc.
    return {"message": "Item created", "item": item}

# Custom response with status code
@app.get("/custom-response")
async def custom():
    return JSONResponse(
        status_code=418,
        content={"message": "I'm a teapot ☕"}
    )