""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
from flask import flash

class Review(Model):
    def __init__(self):
        super(Review, self).__init__()
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

    def insert_review(self, review):
        if not review['review']:
            return False

        query = 'INSERT Into reviews(rating, review, user_id, book_id, created_at) VALUES (:rating, :review, :user_id, :book_id, NOW())'
        data = {'rating': review['rating'], 'review': review['review'], 'user_id': review['user_id'], 'book_id': review['book_id']}
        review_id = self.db.query_db(query, data)
        return review_id









