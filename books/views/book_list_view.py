from django.db.models import Q
from rest_framework import generics, status

from books.helpers.rest_helpers import make_formatted_response
from books.models.book import Book
from books.serializers import BookSerializer


class ListCreateBooksView(generics.ListCreateAPIView):
    def get_queryset(self):
        search_str = self.request.query_params.get('search')
        if search_str:
            queryset = Book.objects.filter(Q(name__icontains=search_str) | Q(country__icontains=search_str) |
                                           Q(publisher__icontains=search_str))
            if search_str.isdigit():
                queryset = queryset.union(Book.objects.filter(Q(release_date__year=search_str)))
        else:
            queryset = Book.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        return make_formatted_response(status.HTTP_200_OK, serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return make_formatted_response(status.HTTP_201_CREATED, serializer.data)

        return make_formatted_response(status_code=status.HTTP_400_BAD_REQUEST, error=serializer.error_messages)
