from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    price: float
    author: str
    is_available: bool

@app.get("/")
def home():
    return "Welcome to FastAPI !!!"

@app.put("/addBook/{book_id}")
def add_book(book_id: int, book: Book = None):
    return {"book_id": book_id, "title_book": book.title}
