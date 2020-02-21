from rest_framework import serializers

from books.models.books import Book, Author, Publisher
from books.models.country import Country


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Author
        fields = ("id", "name")


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    publisher = serializers.SlugRelatedField(slug_field='name', read_only=True)
    country = serializers.SlugRelatedField(slug_field='name', read_only=True)
    authors = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Book
        fields = ("id", "name", "isbn", "authors", "number_of_pages", "publisher", "country", "release_date")

    def to_representation(self, instance):
        data = super(BookSerializer, self).to_representation(instance)

        return data

    def create(self, validated_data):
        request = self.context['request']
        country, _ = Country.objects.get_or_create(name=request.data.get('country'))
        publisher, _ = Publisher.objects.get_or_create(name=request.data.get('publisher'))
        instance = Book.objects.create(country=country, publisher=publisher, **validated_data)
        authors = request.data.get('authors')
        for author in authors:
            author, status = Author.objects.get_or_create(name=author)
            instance.authors.add(author)
        return instance

    def update(self, instance, validated_data):
        request = self.context['request']
        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        country, _ = Country.objects.get_or_create(name=request.data.get('country'))
        instance.country = country
        publisher, _ = Publisher.objects.get_or_create(name=request.data.get('publisher'))
        instance.publisher = publisher
        instance.save()
        authors = request.data.get('authors')
        instance.authors.clear()
        for author in authors:
            author, status = Author.objects.get_or_create(name=author)
            instance.authors.add(author)
        return instance


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class ExternalBooksSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    isbn = serializers.CharField(max_length=50)
    authors = serializers.ListField(child=serializers.CharField(max_length=255))
    number_of_pages = serializers.IntegerField(default=0)
    publisher = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)
    release_date = serializers.DateTimeField(source='released')
