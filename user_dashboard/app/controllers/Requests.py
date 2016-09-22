"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime

class Requests(Controller):
    def __init__(self, action):
        super(Requests, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Request')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
    def add_friend(self, id):
        request = {'user_id': session['id'], 'friend_id': id}
        self.models['Request'].add_friend(request)
        return redirect('/dashboard')

    def confirm_friend(self, id):
        confirm = {'friend_id': session['id'], 'user_id': id}
        self.models['Request'].confirm_friend(confirm)
        return redirect('/dashboard')

    def delete_friend(self, id):
        confirm = {'friend_id': session['id'], 'user_id': id}
        self.models['Request'].delete_friend(confirm)
        return redirect('/dashboard')
   



