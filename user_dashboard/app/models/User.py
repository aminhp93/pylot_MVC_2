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

    def get_all_users(self):
        query = "SELECT * FROM users"
        return self.db.query_db(query)

    def get_user_by_id(self, id):
        query = "SELECT * FROM users WHERE id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def add_user(self, user):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = 0
        # Some basic validation
        if not user['first_name']:
            errors += 1
            flash('Name cannot be blank', 'first_name')
        elif len(user['first_name']) < 2:
            errors += 1
            flash('Name must be at least 2 characters long', 'first_name')

        if not user['first_name']:
            errors += 1
            flash('Name cannot be blank', 'last_name')
        elif len(user['first_name']) < 2:
            errors += 1
            flash('Name must be at least 2 characters long', 'last_name')

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
            password = user['password']
            pw_hash = self.bcrypt.generate_password_hash(password)
            query = "INSERT INTO users (email, first_name, last_name, pw_hash, created_at) VALUES (:email, :first_name, :last_name, :password, NOW())"
            data = {'email': user['email'], 'first_name': user['first_name'], 'last_name': user['last_name'], 'password': pw_hash}
            return self.db.query_db(query, data)

    def check_admin_or_user(self, user):
        if not user['email'] or not user['password']:
            flash('Invalid input', 'login')
            return False

        password = user['password']
        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': user['email']}
        test = self.db.query_db(query, data)

        if test:
            if self.bcrypt.check_password_hash(test[0]['pw_hash'], user['password']):
                return test[0]
            else:
                flash('Password is not match', 'login')
                return False
        return False

    def user_update_1(self, user):
        query = 'UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, level = :level WHERE id = :id'
        data = {'id': user['id'], 'email': user['email'], 'first_name': user['first_name'], 'last_name': user['last_name'], 'level': user['level']}
        return self.db.query_db(query, data)

    def user_update_2(self, user):
        if user['password'] != user['password_confirmation']:
            return False

        query = 'UPDATE users SET pw_hash = :password WHERE id = :id'
        data = {'id': user['id'], 'password': user['password']}
        return self.db.query_db(query, data)

    def user_update_3(self, user):

        query = 'UPDATE users SET description = :description WHERE id = :id'
        data = {'id': user['id'], 'description': user['description']}
        return self.db.query_db(query, data)

    def delete_user(self, id):
        query = "DELETE FROM users WHERE id = :id"
        data = {'id': id}
        return self.db.query_db(query, data)


