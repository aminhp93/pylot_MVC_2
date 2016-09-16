"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random
import datetime

class NinjaGolds(Controller):
    def __init__(self, action):
        super(NinjaGolds, self).__init__(action)
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
        if not 'result' in session:
            session['result'] = 0
        if not 'activities' in session:
            session['activities'] = []
    
        return self.load_view('index.html', activities = session['activities'])

    def action(self, coin, earn, farm):
        time = datetime.datetime.now()
        if earn == 'earn':
            session['activities'].append(['green','Earned ' + str(coin) + 'golds from the ' + str(farm) + str(time)])
        elif earn == 'lost':
            session['activities'].append(['red','Entered a casino and lost ' + str(coin) + 'Ouch...' + str(time)])
        return session['activities']

    def process_money(self):
        if request.form['hidden'] == 'farm':
            coin = random.randint(10, 21)
            session['result'] += coin
            self.action(coin, 'earn', 'farm')
        elif request.form['hidden'] == 'cave':
            coin = random.randint(5, 11)
            session['result'] += coin
            self.action(coin, 'earn', 'cave')
        elif request.form['hidden'] == 'house':
            coin = random.randint(2,6)
            session['result'] += coin
            self.action(coin, 'earn', 'house')
        elif request.form['hidden'] == 'casino':
            coin = random.randint(-50, 50)
            if coin >= 0:
                session['result'] += coin
                self.action(coin, 'earn', 'casino')
            else:
                session['result'] -= coin
                self.action(coin, 'lost', 'casino')

        return redirect('/')


