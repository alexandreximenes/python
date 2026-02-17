from fastapi import FastAPI, HTTPException
import random
import json
import os
import book
from uuid import UUID, uuid4
from fastapi.encoders import jsonable_encoder
import logging

app = FastAPI()

BOOKS_FILE = "books.json"

BOOK_DB = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOK_DB = json.load(f)

@app.get("/")
async def root():
    return {"data": "WELCOME TO LIBRARY API"}


@app.get("/books")
async def books():
    return {"data": BOOK_DB}

@app.get("/books/{book_id}")
async def book_by_id(book_id: int):
    if( book_id < 0 or book_id >= len(BOOK_DB) ):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"data": BOOK_DB[book_id] }

@app.get("/books/random/")
async def book_random():
    return {"data": random.choice(BOOK_DB) }

@app.post("/books")
async def add_book(title: str):
    new_book = {"id": len(BOOK_DB), "title": title}
    with open(BOOKS_FILE, "w") as f:
        BOOK_DB.append(new_book)
        json.dump(BOOK_DB, f)
    return {"data": f'Book "{title}" added successfully with id {new_book["id"]}' }

@app.post("/books/new")
async def add_book(book: book.Book):
    
    new_book = jsonable_encoder(book)
    
    logging.info(f"Adding new book: {new_book}")
    
    with open(BOOKS_FILE, "w") as f:
        BOOK_DB.append(new_book)
        json.dump(BOOK_DB, f)

    return {"data": f'Book "{new_book["title"]}" added successfully with id {new_book["id"]}' }