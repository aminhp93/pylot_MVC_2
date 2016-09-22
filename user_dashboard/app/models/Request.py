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

    def get_all_users_with_status(self, id):
        query = "SELECT table2.status as status_2, table3.status as status_3, users.id, users.first_name, users.last_name, users.email, users.created_at, users.level, table2.user_id, table3.friend_id FROM users LEFT JOIN (SELECT * FROM requests WHERE requests.user_id = :id) as table2 ON users.id = table2.friend_id left join (SELECT * FROM requests WHERE requests.friend_id = :id) as table3 on table3.user_id = users.id"
        data = {'id': id}
        return self.db.query_db(query, data)

    def confirm_friend(self, confirm):
        query = "SELECT * FROM requests WHERE user_id = :user_id AND friend_id = :friend_id"
        data = {'user_id': confirm['user_id'], 'friend_id': confirm['friend_id']}
        id = self.db.query_db(query, data)

        query = 'UPDATE requests SET status = :status WHERE id = :id'
        data = {'id': id[0]['id'], 'status': 'friend'}
        return self.db.query_db(query, data)

    def delete_friend(self, confirm):
        query = "SELECT * FROM requests WHERE user_id = :user_id AND friend_id = :friend_id"
        data = {'user_id': confirm['user_id'], 'friend_id': confirm['friend_id']}
        id = self.db.query_db(query, data)

        query = 'DELETE FROM requests WHERE id = :id'
        data = {'id': id[0]['id'] }
        return self.db.query_db(query, data)




    