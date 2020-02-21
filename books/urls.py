from django.urls import path

from .views.book_details_view import GetPutDeleteBookView
from .views.book_list_view import ListCreateBooksView
from .views.external_books_view import ListIceAndFireBooksView
from .views.login_view import LoginView

urlpatterns = [
    path('auth/login', LoginView.as_view(), name="auth-login"),
    path('external-books', ListIceAndFireBooksView.as_view(), name="external-books-list"),
    path('v1/books/<int:pk>', GetPutDeleteBookView.as_view(), name="book-details"),
    path('v1/books', ListCreateBooksView.as_view(), name="books-list"),
]
