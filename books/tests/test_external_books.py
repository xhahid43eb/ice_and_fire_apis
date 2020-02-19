from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status


class GetAllExternalBooksTest(APITestCase):
    client = APIClient()

    def test_get_all_external_books(self):
        response = self.client.get(
            reverse("external-books-list")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
