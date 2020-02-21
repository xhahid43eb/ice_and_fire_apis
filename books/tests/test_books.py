from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from books.models.books import Book
from books.serializers import BookSerializer


class BaseViewTest(APITestCase):
    client = APIClient()
    book_id = None

    def setUp(self):
        self.create_book()

    def create_book(self):
        response = self.client.post(
            reverse("books-list"),
            {
                "name": "Game of thrones",
                "isbn": "978-0553108032",
                "authors": [
                    "George R. R. Martin"
                ],
                "number_of_pages": 768,
                "publisher": "Bantam Books",
                "country": "United States",
                "release_date": "1999-02-02T00:00:00"
            },
            format='json'
        )
        self.book_id = response.data.get('data').get('id')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class GetAllBooksTest(BaseViewTest):

    def test_get_all_books(self):
        response = self.client.get(
            reverse("books-list")
        )
        expected = Book.objects.all()
        serialized = BookSerializer(expected, many=True)
        self.assertEqual(response.data.get('data'), serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookDetailsTest(BaseViewTest):
    def test_get_book(self):
        response = self.client.get(
            reverse("book-details", kwargs={"pk": self.book_id})
        )
        expected = Book.objects.get(pk=self.book_id)
        serialized = BookSerializer(expected)
        self.assertEqual(response.data.get('data'), serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        response = self.client.put(
            reverse("book-details", kwargs={"pk": self.book_id, }),
            {
                "name": "Game of thrones",
                "isbn": "978-0553108084",
                "authors": [
                    "George R. R. Martin"
                ],
                "number_of_pages": 768,
                "publisher": "Bantam Books",
                "country": "United States",
                "release_date": "1999-02-02T00:00:00"
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(
            reverse("book-details", kwargs={"pk": self.book_id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
