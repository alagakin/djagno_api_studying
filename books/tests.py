from django.test import TestCase
from django.urls import reverse


from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title='Test title',
            subtitle='Test subtitle',
            author='Test author',
            isbn='1234567890123'
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'Test title')
        self.assertEqual(self.book.subtitle, 'Test subtitle')
        self.assertEqual(self.book.author, 'Test author')
        self.assertEqual(self.book.isbn, '1234567890123')

    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test title')
        self.assertContains(response, 'Test subtitle')
        self.assertContains(response, 'Test author')
        self.assertContains(response, '1234567890123')
        self.assertTemplateUsed(response, 'book_list.html')
