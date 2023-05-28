from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

mongo_host = os.environ.get('MONGO_HOST')
# MongoDB connection
client = MongoClient(f"mongodb://{mongo_host}:27017")
db = client["booksdb"]
collection = db["books"]

@app.route("/api/books", methods=["GET"])
def get_books():
    books = collection.find()
    return jsonify([{"id": str(book["_id"]), "title": book["title"], "author": book["author"], "year": book["year"]} for book in books])

@app.route("/api/books/<book_id>", methods=["GET"])
def get_book(book_id):
    book = collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return jsonify({"id": str(book["_id"]), "title": book["title"], "author": book["author"], "year": book["year"]})
    else:
        return jsonify({"message": "Book not found"}), 404

@app.route("/api/books", methods=["POST"])
def add_book():
    book_data = request.get_json()
    book_id = collection.insert_one(book_data).inserted_id
    return jsonify({"id": str(book_id)})

@app.route("/api/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    book_data = request.get_json()
    collection.update_one({"_id": ObjectId(book_id)}, {"$set": book_data})
    return jsonify({"message": "Book updated successfully"})

@app.route("/api/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    collection.delete_one({"_id": ObjectId(book_id)})
    return jsonify({"message": "Book deleted successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

