"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Users'
routes['GET']['/signin'] = 'Users#signin'

routes['GET']['/dashboard/admin'] = 'Users#admin_show'
routes['POST']['/users/admin_add'] = 'Users#admin_add'
routes['GET']['/users/new'] = 'Users#new'
routes['GET']['/users/edit/<int:id>'] = 'Users#admin_edit'
routes['POST']['/admin/update1/<int:id>'] = "Users#admin_update_1"
routes['POST']['/admin/update2/<int:id>'] = "Users#admin_update_2"
routes['POST']['/admin/update3/<int:id>'] = "Users#admin_update_3"
routes['POST']['/users/delete/<int:id>'] = 'Users#delete'

routes['GET']['/register'] = 'Users#register'
routes['POST']['/users/add'] = 'Users#add'
routes['GET']['/dashboard'] = 'Users#user_show'
routes['GET']['/users/profile/<int:id>'] = 'Users#profile'
routes['GET']['/users/edit'] = 'Users#user_edit'
routes['POST']['/users/update1'] = "Users#user_update_1"
routes['POST']['/users/update2'] = "Users#user_update_2"
routes['POST']['/users/update3'] = "Users#user_update_3"

routes['POST']['/login'] = 'Users#login'
routes['GET']['/users/show/<int:id>'] = 'Users#show'
routes['POST']['/messages/add/<int:id>'] = 'Messages#add'
routes['POST']['/comments/add/<int:id>'] = 'Comments#add'

routes['POST']['/add_friend/<int:id>'] = 'Requests#add_friend'


routes['GET']['/logout'] = 'Users#logout'


"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
