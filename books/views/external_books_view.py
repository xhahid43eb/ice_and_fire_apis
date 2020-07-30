from requests import get
from rest_framework import generics, status

from books.helpers.rest_helpers import make_formatted_response
from books.serializers import ExternalBooksSerializer


class ListIceAndFireBooksView(generics.ListAPIView):

    def get_data_from_iceandfire_api(self, request):
        res = get("https://www.anapioficeandfire.com/api/books", request.query_params)
        return res.json()

    def list(self, request, *args, **kwargs):
        data = self.get_data_from_iceandfire_api(request)
        books_list = ExternalBooksSerializer(data, many=True)
        return make_formatted_response(status.HTTP_200_OK, books_list.data)
