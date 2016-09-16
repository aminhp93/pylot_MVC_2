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
        self.load_model('WelcomeModel')
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
        return "In the Users Controller index"

    def new(self):
        return self.load_view('users/new.html')

    def show(self, id):
        user = [{'id': 1, "name": 'MichealChoid', "Hobby": "basketball"}]
        return self.load_view('users/show.html', user = user[0])

    def test(self, color, id):
        print "color {} and id is {}".format(color, id)
        return self.load_view("hello.html", color = color, id = id)

    def test_2(self):
        return self.load_view('users/test.html')


