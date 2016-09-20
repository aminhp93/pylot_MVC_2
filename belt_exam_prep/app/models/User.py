""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
from flask import flash

class User(Model):
    def __init__(self):
        super(User, self).__init__()
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
    def get_user_by_id(self, id):
        query = "SELECT * from users where id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def add_user(self, user):
        
        query = "INSERT into users (name, alias, email, password, created_at) values(:name, :alias, :email, :password, NOW())"
        data = {'name': user['name'], 'alias': user['alias'], 'email': user['email'], 'password': user['password']}
        return self.db.query_db(query, data)

    def login(self, user):
        query = 'SELECT * FROM users WHERE email = :email LIMIT 1'
        print user
        data = {'email': user['email']}
        result = self.db.query_db(query, data)
        if result:
            if result[0]['password'] == user['password']:
                return result
            else:
                flash('Invalid password', 'login')
                return False
        flash('Invalid input', 'login')
        return False

    def get_book_by_user_id(self, id):
        query = "SELECT books.created_at, books.id as book_id, users.alias, users.name, users.email, books.title FROM users LEFT JOIN books ON users.id = books.user_id WHERE users.id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)














