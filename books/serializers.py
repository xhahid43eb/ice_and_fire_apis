from rest_framework import serializers

from books.models.books import Book, Author, Publisher
from books.models.country import Country


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)

    class Meta:
        model = Author
        fields = ('id', 'name')


class PublisherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)

    class Meta:
        model = Publisher
        fields = ('id', 'name')


class CountrySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)

    class Meta:
        model = Country
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    publisher = PublisherSerializer(required=True)
    country = CountrySerializer(required=True)
    authors = AuthorSerializer(required=True, many=True)

    class Meta:
        model = Book
        fields = ("id", "name", "isbn", "authors", "number_of_pages", "publisher", "country", "release_date")

    def create(self, validated_data):
        authors = validated_data.pop('authors')
        country = Country.objects.get(**validated_data.pop('country'))
        publisher = Publisher.objects.get(**validated_data.pop('publisher'))
        instance = Book.objects.create(country=country, publisher=publisher, **validated_data)
        for author in authors:
            author = Author.objects.get(**author)
            instance.authors.add(author)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.country = Country.objects.get(**validated_data.get('country', instance.country))
        instance.publisher = Publisher.objects.get(**validated_data.get('publisher', instance.publisher))
        instance.save()
        authors = validated_data.get('authors', instance.authors)
        instance.authors.clear()
        for author in authors:
            author, status = Author.objects.get_or_create(name=author)
            instance.authors.add(author)
        return instance


class ExternalBooksSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    isbn = serializers.CharField(max_length=50)
    authors = serializers.ListField(child=serializers.CharField(max_length=255))
    number_of_pages = serializers.IntegerField(default=0)
    publisher = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)
    release_date = serializers.DateTimeField(source='released')
