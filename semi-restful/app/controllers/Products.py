"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Product')
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
        products = self.models['Product'].get_all_products()
        return self.load_view('index.html', products = products)

    def new(self):
        return self.load_view('new.html')

    def create(self):
        post = request.form

        name = post['name']
        description = post['description']
        price = post['price']
        product = {'name': name, 'description': description, 'price': price}

        self.models['Product'].add_product(product)
        return redirect('/products')

    def show(self, id):
        product = self.models['Product'].get_product_by_id(id)
        return self.load_view('show.html', product = product)

    def edit(self, id):
        product = self.models['Product'].get_product_by_id(id)
        return self.load_view('edit.html', product = product)

    def update(self, id):
        post = request.form

        name = post['name']
        description = post['description']
        price = post['price']
        product = {'id': id, 'name': name, 'description': description, 'price': price}
        print product

        product = self.models['Product'].update_product(product)
        return redirect('/products')

    def destroy(self, id):
    	product = self.models['Product'].delete_product(id)
    	return redirect('/products')

















