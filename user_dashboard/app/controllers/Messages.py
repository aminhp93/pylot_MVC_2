"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Messages(Controller):
    def __init__(self, action):
        super(Messages, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Message')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):        
        return self.load_view('users/index.html')

    def add(self, id):
        message = request.form['message']
        message = {'message': message, 'user_id': str(id)}
        self.models['Message'].add_message(message)
        return redirect('/users/show/' + str(id))
        




