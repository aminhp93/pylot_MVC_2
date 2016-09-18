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
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):        
        return self.load_view('users/index.html')

    def add(self):
        post = request.form
        # collect data
        email = post['email']
        first_name = post['first_name']
        last_name = post['last_name']
        password = post['password']
        password_confirmation = post['password_confirmation']

        user = {'email': email, 'first_name': first_name, 'last_name': last_name, 'password': password, 'password_confirmation': password_confirmation}

        self.models['User'].add_user(user)
        return redirect('/signin')

    def register(self):
        return self.load_view('users/register.html')

    def check(self):
        post = request.form
        email = post['email']
        password = post['password']
        user = {'email': email, 'password': password}
        result = self.models['User'].check_admin_or_user(user)
        print result
        if result['level'] == 'admin':
            return redirect('/dashboard/admin')
        elif result['level'] == 'normal':
            session['id'] = result['id']
            return redirect('/dashboard')
        else:
            return redirect("/users/new")

    def signin(self):

        return self.load_view('users/signin.html')

    def new(self):
        return self.load_view('users/new.html')

    def admin_show(self):
        return self.load_view('users/admin_show.html')

    def user_show(self):
        users = self.models['User'].get_all_users()
        return self.load_view('users/user_show.html', users = users)

    def user_edit(self):
        user = self.models['User'].get_user_by_id(session['id'])
        return self.load_view('users/user_edit.html', user = user[0])

    def user_update_1(self):
        post = request.form
        email = post['email']
        first_name = post['first_name']
        last_name = post['last_name']
        user = {'id': session['id'], 'email': email, 'first_name': first_name, 'last_name': last_name}

        result = self.models['User'].user_update_1(user)
        return redirect('dashboard')

    def user_update_2(self):
        post = request.form
        password = post['password']
        password_confirmation = post['password_confirmation']
        user = {'id': session['id'], 'password': password, 'password_confirmation': password_confirmation}

        result = self.models['User'].user_update_2(user)
        if result == False:
            return redirect('users/edit')
        return redirect('dashboard')

    def user_update_3(self):
        post = request.form
        description = post['description']
        user = {'id': session['id'], 'description': description}
        
        result = self.models['User'].user_update_3(user)
        return redirect('dashboard')



