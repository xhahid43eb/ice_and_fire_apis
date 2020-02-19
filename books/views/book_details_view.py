from django.shortcuts import get_object_or_404
from rest_framework import generics, status

from books.helpers.rest_helpers import make_formatted_response
from books.models.book import Book
from books.serializers import BookSerializer


class GetPutDeleteBookView(generics.RetrieveUpdateDestroyAPIView):

    def get_queryset(self):
        return get_object_or_404(Book, pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        serializer = BookSerializer(self.get_queryset())
        return make_formatted_response(status.HTTP_200_OK, serializer.data)

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return make_formatted_response(
                status_code=status.HTTP_200_OK,
                data=serializer.data,
                message=f'The book {queryset.name} was updated successfully')

        return make_formatted_response(status_code=status.HTTP_400_BAD_REQUEST, error=serializer.error_messages)

    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return make_formatted_response(
            status_code=status.HTTP_204_NO_CONTENT,
            message=f'The book {queryset.name} was deleted successfully'
        )
