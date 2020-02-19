from requests import get
from rest_framework import generics, status

from books.helpers.rest_helpers import make_formatted_response


def format_books_data(book):
    return {
        'name': book['name'],
        'isbn': book['isbn'],
        'authors': book['authors'],
        'number_of_pages': book['numberOfPages'],
        'publisher': book['publisher'],
        'country': book['country'],
        'release_date': book['released']
    }


class ListIceAndFireBooksView(generics.ListAPIView):

    def list(self, request, *args, **kwargs):
        res = get("https://www.anapioficeandfire.com/api/books", request.query_params)
        books_list = [format_books_data(book) for book in res.json()]
        return make_formatted_response(status.HTTP_200_OK, books_list)
