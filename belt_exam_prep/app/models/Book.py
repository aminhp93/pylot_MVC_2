""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
from flask import flash

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """

    def insert_book(self, book):
        if not book['title'] or not book['review']:
            return False

        if book['new_author'] == "":
            author = book['author_list']
        else:
            author = book['new_author']

        query = "INSERT INTO books (title, author, review, rating, created_at) VALUES (:title, :author, :review, :rating, NOW())"
        data = {'title': book['title'], 'author': author, 'rating': book['rating'], 'review': book['review']}
        result = self.db.query_db(query, data)
        return result

    def get_book_by_id(self, id):
        query = "SELECT * FROM books WHERE id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def get_reviews_by_book_id(self, id):
        query = "SELECT books.user_id, books.review, books.created_at, users.name, books.rating FROM books LEFT JOIN users ON users.id = books.user_id WHERE books.user_id = :user_id"
        data = {'user_id': id}
        return self.db.query_db(query, data)

    def get_all_books(self):
        query = "SELECT * FROM books"
        return self.db.query_db(query)








