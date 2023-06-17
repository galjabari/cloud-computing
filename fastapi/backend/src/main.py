from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = FastAPI()

mongo_host = os.environ.get('MONGO_HOST')
# MongoDB connection
client = MongoClient(f"mongodb://{mongo_host}:27017")
db = client["booksdb"]
collection = db["books"]

@app.get("/api/books")
def get_books():
    books = collection.find()
    return [
        {"id": str(book["_id"]), "title": book["title"], "author": book["author"], "year": book["year"]}
        for book in books
    ]

@app.get("/api/books/{book_id}")
def get_book(book_id: str):
    book = collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return {"id": str(book["_id"]), "title": book["title"], "author": book["author"], "year": book["year"]}
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@app.post("/api/books")
def add_book(book_data: dict):
    book_id = collection.insert_one(book_data).inserted_id
    return {"id": str(book_id)}

@app.put("/api/books/{book_id}")
def update_book(book_id: str, book_data: dict):
    collection.update_one({"_id": ObjectId(book_id)}, {"$set": book_data})
    return {"message": "Book updated successfully"}

@app.delete("/api/books/{book_id}")
def delete_book(book_id: str):
    collection.delete_one({"_id": ObjectId(book_id)})
    return {"message": "Book deleted successfully"}
