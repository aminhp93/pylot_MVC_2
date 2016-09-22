""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Message_friend(Model):
    def __init__(self):
        super(Message_friend, self).__init__()

    def insert_message_friend(self, message):
        query = "INSERT INTO friend_message(message, user_id, friend_id, created_at) VALUES (:message, :user_id, :friend_id, NOW())"
        data = {'message': message['message'], 'user_id': message['user_id'], 'friend_id': message['friend_id']}
        return self.db.query_db(query, data)

    def get_all_messages(self, info):
        query = "SELECT * FROM friend_message WHERE user_id = :user_id, message_id = :message_id"
        data = {'user_id': info['user_id'], 'message_id': info['message_id']}
        return self.db.query_db(query)

