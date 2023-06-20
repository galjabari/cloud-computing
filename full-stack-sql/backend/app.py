from flask import Flask, jsonify, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'secret'
app.config['MYSQL_DATABASE_DB'] = 'books'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)

@app.route('/setup', methods=['GET'])
def setup_database():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS books")
        cursor.execute("USE books")

        # Create books table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                year VARCHAR(4) NOT NULL
            )
        """)

        cursor.close()
        conn.close()
        return 'Database setup completed successfully!'
    except Exception as e:
        return str(e)

@app.route('/books', methods=['GET'])
def get_all_books():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        books = []
        for row in rows:
            book = {
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'year': row[3]
            }
            books.append(book)
        cursor.close()
        conn.close()
        return jsonify(books)
    except Exception as e:
        return str(e)


@app.route('/books', methods=['POST'])
def add_book():
    try:
        title = request.json['title']
        author = request.json['author']
        year = request.json['year']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
        conn.commit()
        cursor.close()
        conn.close()
        return 'Book added successfully!'
    except Exception as e:
        return str(e)


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    try:
        title = request.json['title']
        author = request.json['author']
        year = request.json['year']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title=%s, author=%s, year=%s WHERE id=%s", (title, author, year, id))
        conn.commit()
        cursor.close()
        conn.close()
        return 'Book updated successfully!'
    except Exception as e:
        return str(e)


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return 'Book deleted successfully!'
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
