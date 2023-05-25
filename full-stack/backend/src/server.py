from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

mongo_host = os.environ.get('MONGO_HOST')
# MongoDB connection
client = MongoClient(f"mongodb://{mongo_host}:27017")
db = client['books']
collection = db['books']

@app.route('/api/books', methods=['GET'])
def get_books():
    books = list(collection.find())
    return jsonify(books)

@app.route('/api/books', methods=['POST'])
def add_book():
    book = request.json
    result = collection.insert_one(book)
    book['_id'] = str(result.inserted_id)
    return jsonify(book)

@app.route('/api/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    result = collection.delete_one({'_id': ObjectId(book_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'message': 'Book not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
