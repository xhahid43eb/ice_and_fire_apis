from rest_framework import serializers

from books.models.books import Book, Author, Publisher
from books.models.country import Country


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name')


class PublisherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publisher
        fields = ('id', 'name')


class CountrySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ("id", "name", "isbn", "authors", "number_of_pages", "publisher", "country", "release_date")

    def to_representation(self, instance):
        data = super(BookSerializer, self).to_representation(instance)
        data['country'] = CountrySerializer(instance.country).data
        data['publisher'] = PublisherSerializer(instance.publisher).data
        data['authors'] = AuthorSerializer(instance.authors, many=True).data
        return data


class ExternalBooksSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    isbn = serializers.CharField(max_length=50)
    authors = serializers.ListField(child=serializers.CharField(max_length=255))
    number_of_pages = serializers.IntegerField(default=0)
    publisher = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)
    release_date = serializers.DateTimeField(source='released')
