""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
from flask import flash
import re

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
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = 0
        # Some basic validation
        if not user['name']:
            errors += 1
            flash('Name cannot be blank', 'name')
        elif len(user['name']) < 2:
            errors += 1
            flash('Name must be at least 2 characters long', 'name')

        if not user['email']:
            errors += 1
            flash('Email cannot be blank', 'email')
        elif not EMAIL_REGEX.match(user['email']):
            errors += 1
            flash('Email format must be valid!', 'email')

        if not user['password']:
            errors += 1
            flash('Password cannot be blank', 'password')
        elif len(user['password']) < 8:
            errors += 1
            flash('Password must be at least 8 characters long', 'password')
        elif user['password'] != user['password_confirmation']:
            errors += 1
            flash('Password and confirmation must match!', 'password')

        # If we hit errors, return them, else return True.
        if errors > 0:
            return False
        else:
            flash('You successfully registerd. Please log in.', 'login_success')
            password = user['password']

            pw_hash = self.bcrypt.generate_password_hash(password)

            query = "INSERT into users (name, alias, email, password, created_at) values(:name, :alias, :email, :password, NOW())"
            data = {'name': user['name'], 'alias': user['alias'], 'email': user['email'], 'password': pw_hash}
            return self.db.query_db(query, data)

    def login(self, user):
        if not user['email'] or not user['password']:
            flash('Invalid input', 'login')
            return False

        query = 'SELECT * FROM users WHERE email = :email LIMIT 1'
        data = {'email': user['email']}
        result = self.db.query_db(query, data)

        if result:
            if self.bcrypt.check_password_hash(result[0]['password'], user['password']):
                return result[0]['id']
            else:
                flash('Invalid password', 'login')
                return False
        return False

    def get_book_by_user_id(self, id):
        query = "SELECT books.created_at, books.id as book_id, books.user_id, users.alias, users.name, users.email, books.title FROM users LEFT JOIN books ON users.id = books.user_id WHERE users.id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def get_review_by_user_id(self, id):
        query = "SELECT users.email, users.alias, users.name, books.title, reviews.book_id FROM users LEFT JOIN reviews ON users.id = reviews.user_id LEFT JOIN books ON reviews.book_id = books.id WHERE users.id = :id GROUP BY books.title"
        data = {'id': id}
        return self.db.query_db(query, data)














