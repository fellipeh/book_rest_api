# book_rest_api
REST api built using flask

#### How to use
- Create a virtual enviroment
- install requirements ( `$ pip install -r ./requirements.txt` )
- start your virtualenv 
- type these:

`$ python app.py`

These are the endpoints:

`/book`  - GET

Show all books

`/book`  - POST
Add new book, send a json with these fields(title, author)

`/book/<id>` - GET
Get book detail by id

`/book/<id>` - PUT
Update the book by ID (send a json with fields)

`/book/<id>` - DELETE
Delete book by id
