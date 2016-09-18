"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Comments(Controller):
    def __init__(self, action):
        super(Comments, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Comment')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):        
        return self.load_view('users/index.html')

    def add(self, id):
        comment = request.form['comment']
        comment = {'comment': comment, 'user_id': session['id'], 'message_id': id}
        self.models['Comment'].add_comment(comment)
        return redirect('/users/show/' + str(session['id']))

