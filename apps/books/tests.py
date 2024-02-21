from django.test import TestCase
from django.urls import reverse

from apps.books.models import Book, BookReview
from apps.users.models import User

from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import AddBookReviewForm


# class BookTestCase(TestCase):
#     def test_no_books(self):
#         response = self.client.get(reverse("books:book-list"))
#         self.assertContains(response, "No Books")
#         self.assertEquals(response.status_code, 200)
#
#     def test_book_list(self):
#         book1 = Book.objects.create(title="Book1", description="Description1", slug="book1", published="2000-12-12",
#                                     isbn="218983981", page=123)
#         book2 = Book.objects.create(title="Book2", description="Description2", slug="book2", published="2000-12-12",
#                                     isbn="218983911", page=123)
#
#         response = self.client.get(reverse("books:book-list"))
#         self.assertContains(response, book1.title)
#         self.assertContains(response, book1.description)
#         self.assertContains(response, book2.title)
#         self.assertContains(response, book2.description)
#         self.assertEquals(response.status_code, 200)
#
#     def test_book_detail(self):
#         book1 = Book.objects.create(title="Book1", description="Description1", slug="book1", published="2000-12-12",
#                                     isbn="218983981", page=123)
#         user = User.objects.create(
#             username="test",
#             middle_name="Test1"
#         )
#         user.set_password("testpass")
#         user.save()
#         review = BookReview.objects.create(
#             user=user,
#             book=book1,
#             body="Body1",
#             rating=5
#         )
#         response = self.client.get(reverse("books:book-detail", kwargs={"slug": book1.slug}))
#         self.assertEquals(response.status_code, 200)
#         self.assertContains(response, book1.title)
#         self.assertContains(response, book1.description)
#         self.assertContains(response, book1.page)
#         self.assertContains(response, book1.isbn)
#         self.assertContains(response, 12)
#         self.assertContains(response, 2000)
#         self.assertContains(response, "Dec")
#         self.assertContains(response, review.rating)
#         self.assertContains(response, review.user.username)
#         self.assertContains(response, review.body)


class AddReviewViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.client = Client()
        self.user = User.objects.create_user(username="Userbek", password="testpassword")
        self.book = Book.objects.create(title="Test Book", author="Test Userbek", description="Test Description")
        self.valid_form = {
            "body": "Test review body",
            "rating": 4
        }

    def test_add_review(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("add_review", kwargs={"pk": self.book.id}), data=self.valid_form)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BookReview.objects.count(), 1)
