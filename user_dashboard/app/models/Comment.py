""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Comment(Model):
    def __init__(self):
        super(Comment, self).__init__()

    def add_comment(self, comment):
    	query = "INSERT INTO comments(comment, user_id, message_id, created_at) VALUES (:comment, :user_id, :message_id, NOW())"
    	data = {'comment': comment['comment'], 'user_id': comment['user_id'], 'message_id': comment['message_id']}
    	return self.db.query_db(query, data)

    def get_all_comments(self):
    	query = "SELECT users.first_name, comments.comment, comments.message_id FROM comments LEFT JOIN users ON comments.user_id = users.id ORDER BY comments.created_at DESC"
    	return self.db.query_db(query)




    