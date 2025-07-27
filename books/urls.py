from django.urls import path
from .views import RegisterView, BookListCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]