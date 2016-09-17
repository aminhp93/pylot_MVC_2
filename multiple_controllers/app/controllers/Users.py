"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.load_model('Message')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        users = self.models['User'].get_all_users()
        messages = self.models['Message'].get_3_messages()
        return self.load_view('users/index.html', users = users, messages = messages)

    def new(self):
        return self.load_view('users/new.html')
        
    def create(self):
        name = request.form['name']
        email = request.form['email']
        user = {'name': name, 'email': email}

        self.models['User'].add_user(user)
        return redirect('/users')



