from django.urls import path

from .views.book_details_view import GetPutDeleteBookView
from .views.book_list_view import ListCreateBooksView
from .views.external_books_view import ListIceAndFireBooksView

urlpatterns = [
    path('external-books', ListIceAndFireBooksView.as_view(), name="external-books-list"),
    path('v1/books/<int:pk>', GetPutDeleteBookView.as_view(), name="book-details"),
    path('v1/books', ListCreateBooksView.as_view(), name="books-list"),
]
