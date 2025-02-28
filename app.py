from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (for demonstration purposes)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
]


# GET all books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


# GET a specific book
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)


# POST a new book
@app.route("/books", methods=["POST"])
def create_book():
    if not request.json or "title" not in request.json or "author" not in request.json:
        return jsonify({"error": "Title and author are required"}), 400

    new_book = {
        "id": max(book["id"] for book in books) + 1,
        "title": request.json["title"],
        "author": request.json["author"],
    }
    books.append(new_book)
    return jsonify(new_book), 201


# PUT/UPDATE a book
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    if not request.json:
        return jsonify({"error": "No data provided"}), 400

    book["title"] = request.json.get("title", book["title"])
    book["author"] = request.json.get("author", book["author"])
    return jsonify(book)


# DELETE a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    books.remove(book)
    return jsonify({"message": "Book deleted successfully"}), 200


# Home page endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "name": "Books API",
            "version": "1.0",
            "description": "A simple REST API for managing books",
            "endpoints": {
                "GET /": "This help message",
                "GET /books": "Get all books",
                "GET /books/<id>": "Get a specific book",
                "POST /books": "Create a new book",
                "PUT /books/<id>": "Update a book",
                "DELETE /books/<id>": "Delete a book",
            },
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
