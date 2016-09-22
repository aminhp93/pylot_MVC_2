"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Message_friends(Controller):
    def __init__(self, action):
        super(Message_friends, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Message_friend')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """

    def message_friend(self, friend_id):
        info = {'user_id': session['id'], 'friend_id': friend_id}
        messages = self.models['Message_friend'].get_message_friend(info)

        return self.load_view('/users/message_friend.html', friend_id = friend_id, messages = messages)

    def insert_message_friend(self, id):
        message = {'message': request.form['message'], 'user_id': session['id'], 'friend_id': id}
        self.models['Message_friend'].insert_message_friend(message)
        return redirect('/message_friend/' + str(id))

        




