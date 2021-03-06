"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
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


        return self.load_view('index.html')

    def create(self):
        if 'num' not in session:
            session['num'] = 0
        session['num'] += 1

        flash('Thanks for submitting this form. You have submitted this form' + str(session['num']) + 'times.')
        # print get_flashed_messages()

        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']

        return self.load_view('result.html', name = name, location = location, language = language, comment = comment)

