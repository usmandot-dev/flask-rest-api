from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_books():
    with open("books.json") as f:
        return json.load(f)

@app.route("/")
def welcome():
    return jsonify({"message": "Welcome to the Book API!"})

@app.route("/books", methods=["GET"])
def get_books():
    books = load_books()
    return jsonify(books)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    books = load_books()
    book = next((b for b in books if b["id"] == book_id), None)
    return jsonify(book) if book else jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
