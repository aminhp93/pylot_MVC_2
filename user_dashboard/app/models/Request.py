""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Request(Model):
    def __init__(self):
        super(Request, self).__init__()

    def add_friend(self, request):
        query = "INSERT INTO requests (user_id, friend_id) VALUES (:user_id, :friend_id)"
        data = {'user_id': request['user_id'], 'friend_id': request['friend_id']}
        return self.db.query_db(query, data)

    def get_all_users_with_status(self):
        query = "SELECT users.id, users.first_name, users.last_name, users.email, users.created_at, users.level, requests.status FROM users LEFT JOIN requests ON users.id = requests.user_id"
        return self.db.query_db(query)



    