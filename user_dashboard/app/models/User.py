""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

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
        query = "INSERT INTO users (email, first_name, last_name, pw_hash, created_at) VALUES (:email, :first_name, :last_name, :password, NOW())"
        data = {'email': user['email'], 'first_name': user['first_name'], 'last_name': user['last_name'], 'password': user['password']}
        return self.db.query_db(query, data)

    def check_admin_or_user(self, user):
        if not user['email'] or not user['password']:
            return False

        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': user['email']}
        test = self.db.query_db(query, data)

        if test:
            if test[0]['pw_hash'] == user['password']:
                return test[0]
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




















