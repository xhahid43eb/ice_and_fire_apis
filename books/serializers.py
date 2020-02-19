from rest_framework import serializers

from books.models.book import Book


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.ListField(child=serializers.CharField())
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ("id", "name", "isbn", "authors", "number_of_pages", "publisher", "country", "release_date")

    def to_representation(self, instance):
        data = super(BookSerializer, self).to_representation(instance)
        if type(instance.authors) == str:
            data['authors'] = instance.get_authors()
        return data
