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

    def message_friend(self, id):

        return self.load_view('/users/message_friend.html')

    def insert_message_friend(self, id):
        message = {'message': request.form['message'] }
        id = self.models['Message'].insert_message_friend(message)
        return redirect('/message_friend/' + str(id))

        




