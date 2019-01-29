from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'books.sqlite')
app.config["DEBUG"] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

db.create_all()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(120))

    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'title', 'author')


book_schema = BookSchema()
books_schema = BookSchema(many=True)


# endpoint to create new book
@app.route("/book", methods=["POST"])
def add_book():
    title = request.json['title']
    author = request.json['author']

    new_book = Book(title, author)

    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book)


# endpoint to show all books
@app.route("/book", methods=["GET"])
def get_book():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result.data)


# endpoint to get book detail by id
@app.route("/book/<id>", methods=["GET"])
def book_detail(id):
    book = Book.query.get(id)
    return book_schema.jsonify(book)


# endpoint to update book
@app.route("/book/<id>", methods=["PUT"])
def book_update(id):
    book = Book.query.get(id)
    title = request.json['title']
    author = request.json['author']

    book.title = title
    book.author = author

    db.session.commit()
    return book_schema.jsonify(book)


# endpoint to delete book
@app.route("/book/<id>", methods=["DELETE"])
def book_delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return book_schema.jsonify(book)


if __name__ == '__main__':
    app.run(debug=True)
