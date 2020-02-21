from requests import get
from rest_framework import generics, status

from books.helpers.rest_helpers import make_formatted_response
from books.serializers import ExternalBooksSerializer


class ListIceAndFireBooksView(generics.ListAPIView):

    def get_queryset(self, request):
        res = get("https://www.anapioficeandfire.com/api/books", request.query_params)
        return res.json()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset(request)
        books_list = ExternalBooksSerializer(queryset, many=True)
        return make_formatted_response(status.HTTP_200_OK, books_list.data)
