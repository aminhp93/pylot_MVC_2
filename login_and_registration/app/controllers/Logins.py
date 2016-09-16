"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Logins(Controller):
    def __init__(self, action):
        super(Logins, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Login')
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

    def add(self):
        post = request.form

        # gather data from form
        first_name = post['first_name']
        last_name = post['last_name']
        email = post['email']
        pw_hash = post['password']
        confirm = post['password_confirm']
        user = {'first_name': first_name, 'last_name': last_name, 'email': email, 'pw_hash': pw_hash, 'confirm': confirm}

        current_user = self.models['Login'].add_user(user)
        print current_user
        if current_user != False:
            session['id'] = current_user['id']
            flash("Successfully registered")
            return redirect('/success')
        return redirect('/')

    def login(self):
        post = request.form

        email_login = post['email_login']
        password_login = post['password_login']
        user = {'email': email_login, 'password': password_login}

        current_user = self.models['Login'].login_user(user)
        print current_user
        if current_user != False:
            session['id'] = current_user['id']
            flash('Successfully logged in')
            return redirect('/success')
        return redirect('/')

    def success(self):
        user = self.models['Login'].get_user_by_id(session['id'])
        return self.load_view('show.html', user = user)






