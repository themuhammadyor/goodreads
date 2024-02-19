from django.urls import path

from apps.books.views import BookListView, BookDetailView, AuthorListView

app_name = "books"

urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book-detail"),
    path('books/', AuthorListView.as_view(), name="author-list")
    # path('<pk>/', AuthorView.as_view(), name="book-detail"),
    # path('<pk>/', GenreView.as_view(), name="book-detail"),
]
