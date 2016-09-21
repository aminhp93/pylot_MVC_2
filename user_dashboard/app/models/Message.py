""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()

    def add_message(self, message):
        query = "INSERT INTO messages(message, user_id, created_at) VALUES (:message, :user_id, NOW())"
        data = {'message': message['message'], 'user_id': message['user_id']}
        return self.db.query_db(query, data)

    def get_all_messages(self):
        query = "SELECT messages.message, messages.created_at, messages.id, users.first_name, messages.user_id FROM messages LEFT JOIN users ON users.id = messages.user_id ORDER BY created_at DESC"
        return self.db.query_db(query)



    