from django.contrib import admin

from books.models.books import Book, Author, Publisher
from books.models.country import Country

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Country)
