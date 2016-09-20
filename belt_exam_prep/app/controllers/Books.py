"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Book')
        self.load_model('Review')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def add_book(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
       
        return self.load_view('add_book.html')

    def insert_book(self):
        post = request.form

        title = post['title']
        author_list = post['author_list']
        new_author = post['new_author']
        review = post['review']
        rating = post['rating']
        user_id = session['id']

        book = {'title': title, 'author_list': author_list, 'new_author': new_author, 'user_id': user_id}

        book_id = self.models['Book'].insert_book(book)
        if book_id == False:
            return redirect('/books/add')

        review = {'rating': rating, 'review': review, 'book_id': book_id, 'user_id': session['id']}
        review_id = self.models['Review'].insert_review(review)
        if review_id == False:
            return redirect('/books/add')

        return redirect('/books/' + str(book_id))

    def show_one_book(self, id):
        book = self.models['Book'].get_book_by_id(id)
        reviews = self.models['Book'].get_reviews_by_book_id(id)
        return self.load_view('show_one_book.html', book = book, reviews = reviews)

    