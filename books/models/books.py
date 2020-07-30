from django.db import models

from .country import Country


class Author(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)
    isbn = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    number_of_pages = models.PositiveIntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    release_date = models.DateTimeField()

    def __str__(self):
        return self.name
