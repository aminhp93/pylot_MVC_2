"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.load_model('Message')
        self.load_model('Comment')
        self.load_model("Request")
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        if not 'id' in session:
            session['id'] = ""
        if not 'level' in session:
            session['level'] = ""
        print session.items()
        return self.load_view('users/index.html')

    def signin(self):
        return self.load_view('users/signin.html')

    def register(self):
        return self.load_view('users/register.html')

    def add(self):
        post = request.form
        # collect data
        email = post['email']
        first_name = post['first_name']
        last_name = post['last_name']
        password = post['password']
        password_confirmation = post['password_confirmation']

        user = {'email': email, 'first_name': first_name, 'last_name': last_name, 'password': password, 'password_confirmation': password_confirmation}

        result = self.models['User'].add_user(user)
        if result == False:
            return redirect('/register')
        return redirect('/signin')

    def login(self):
        post = request.form
        email = post['email']
        password = post['password']
        user = {'email': email, 'password': password}
        result = self.models['User'].check_admin_or_user(user)

        if result != False:
            if result['level'] == 'admin':
                session['level'] = 'admin'
                session['id'] = result['id']
                return redirect('/dashboard/admin')
            elif result['level'] == 'normal':
                session['id'] = result['id']
                session['level'] = 'normal'
                return redirect('/dashboard')
        return redirect("/signin")

# ======================================================================================
#         # Admin 
# ======================================================================================
    
    def admin_show(self):
        if not 'level' in session or session['level'] != "admin":
            return redirect('/')
        users = self.models['User'].get_all_users()
        return self.load_view('users/admin_show.html', users = users)

    def new(self):
        return self.load_view('users/new.html')

    def admin_add(self):
        post = request.form
        # collect data
        email = post['email']
        first_name = post['first_name']
        last_name = post['last_name']
        password = post['password']
        password_confirmation = post['password_confirmation']

        user = {'email': email, 'first_name': first_name, 'last_name': last_name, 'password': password, 'password_confirmation': password_confirmation}

        self.models['User'].add_user(user)
        return redirect('/dashboard/admin')

    def admin_edit(self, id):
        if not 'level' in session or session['level'] != "admin":
            return redirect('/')
        user = self.models['User'].get_user_by_id(id)
        return self.load_view('users/admin_edit.html', user = user[0])

    def admin_update_1(self, id):
        post = request.form
        email = post['email']
        first_name = post['first_name']
        last_name = post['last_name']
        level = post['level']
        level = level.lower()
        user = {'id': id, 'email': email, 'first_name': first_name, 'last_name': last_name, 'level': level}

        result = self.models['User'].user_update_1(user)
        return redirect('/dashboard/admin')

    def admin_update_2(self, id):
        post = request.form
        password = post['password']
        password_confirmation = post['password_confirmation']
        user = {'id': id, 'password': password, 'password_confirmation': password_confirmation}

        result = self.models['User'].user_update_2(user)
        if result == False:
            return redirect('users/edit')
        return redirect('/dashboard/admin')

    def admin_update_3(self, id):
        post = request.form
        description = post['description']
        user = {'id': id, 'description': description}
        
        result = self.models['User'].user_update_3(user)
        return redirect('/dashboard/admin')

    def delete(self, id):
        self.models['User'].delete_user(id)
        return redirect('/dashboard/admin')

# ======================================================================================
#         # USER 
# ======================================================================================
    
    def user_show(self):
        if not 'id' in session or session['id'] == "":
            return redirect('/')
        users = self.models['Request'].get_all_users_with_status(session['id'])
        return self.load_view('users/user_show.html', users = users)

    def user_edit(self):
        if not 'id' in session or session['id'] == "":
            return redirect('/')
        user = self.models['User'].get_user_by_id(session['id'])
        return self.load_view('users/user_edit.html', user = user[0])

    def user_update_1(self):
        post = request.form
        email = post['email']
        first_name = post['first_name']
        last_name = post['last_name']
        level = post['level']
        level = level.lower()
        user = {'id': session['id'], 'email': email, 'first_name': first_name, 'last_name': last_name, 'level': level}

        result = self.models['User'].user_update_1(user)
        return redirect('/dashboard')

    def user_update_2(self):
        post = request.form
        password = post['password']
        password_confirmation = post['password_confirmation']
        user = {'id': session['id'], 'password': password, 'password_confirmation': password_confirmation}

        result = self.models['User'].user_update_2(user)
        if result == False:
            return redirect('users/edit')
        return redirect('/dashboard')

    def user_update_3(self):
        post = request.form
        description = post['description']
        user = {'id': session['id'], 'description': description}
        
        result = self.models['User'].user_update_3(user)
        return redirect('/dashboard')

    def profile(self, id):
        user = self.models['User'].get_user_by_id(id)
        return self.load_view('users/profile.html', user = user[0])

# ======================================================================================
#         # BOTH 
# ======================================================================================
    
    def show(self, id):
        time = strftime("%d %b %Y %H:%M:%S")
        user = self.models['User'].get_user_by_id(id)

        messages = self.models['Message'].get_all_messages()

        comments = self.models['Comment'].get_all_comments()

        return self.load_view('users/test_app.html', user = user[0], messages = messages, comments = comments, time = time )

    def logout(self):
        session.pop('id')
        session.pop('level')
        return redirect('/')



