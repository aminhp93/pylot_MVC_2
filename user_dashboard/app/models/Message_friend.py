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
        query = "INSERT INTO message_friend(message, user_id, friend_id, created_at) VALUES (:message, :user_id, :friend_id, NOW())"
        data = {'message': message['message'], 'user_id': message['user_id'], 'friend_id': message['friend_id']}
        return self.db.query_db(query, data)

    def get_message_friend(self, info):
        query = "SELECT message_friend.message, users.first_name, message_friend.user_id FROM message_friend LEFT JOIN users ON message_friend.user_id = users.id WHERE (user_id = :user_id and friend_id = :friend_id) OR (user_id = :friend_id and friend_id = :user_id) ORDER BY message_friend.created_at"
        data = {'user_id': info['user_id'], 'friend_id': info['friend_id']}
        return self.db.query_db(query, data)

