""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
# import flash

class Login(Model):
    def __init__(self):
        super(Login, self).__init__()
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
    def add_user(self, user):

        # check validation
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

        errors = []
        if not user['first_name']:
            errors.append("First name can not be blank")
        elif len(user['first_name']) < 2:
            errors.append('Name must be at least 2 chars long')

        if not user['email']:
            errors.append('Email can not be blank')
        elif not EMAIL_REGEX.match(user['email']):
            errors.append('Email format must be valid')

        if not user['pw_hash']:
            errors.append('Password can not be blank')

        if errors:
            return False
        else:
            # flash('Successfully registerd!')
            password = user['pw_hash']
            pw_hash = self.bcrypt.generate_password_hash(password)
            insert_user_query = 'INSERT into login (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())'
            data = {'first_name': user['first_name'], 'last_name': user['last_name'], 'email': user['email'], 'pw_hash': pw_hash}
            self.db.query_db(insert_user_query, data)

            get_user_query = 'SELECT * FROM login ORDER BY id DESC LIMIT 1'
            user = self.db.query_db(get_user_query)
            return user[0]

    def login_user(self, user):
        errors = []
        if not user['email']:
            errors.append('Email can not be blank')
        if not user['password']:
            errors.append('Password can not be blank')
        if errors:
            return False
        else:
            password = user['password']
            get_user_query = "SELECT * FROM login WHERE email = :email LIMIT 1"
            data = {'email': user['email']}
            logged_user = self.db.query_db(get_user_query, data)
            if logged_user:
                if self.bcrypt.check_password_hash(logged_user[0]['pw_hash'], password):
                    return logged_user[0]
            return False

    def get_user_by_id(self, id):
        get_user_query = 'SELECT * FROM login WHERE id = :id  LIMIT 1'
        data = {'id': id}
        user = self.db.query_db(get_user_query, data)
        return user[0]





