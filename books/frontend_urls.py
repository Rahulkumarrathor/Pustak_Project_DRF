from django.urls import path
from . import frontend_views

urlpatterns = [
    path('login/', frontend_views.login_view, name='login'),
    path('books-page/', frontend_views.books_view, name='books-page'),
    path('add-book/', frontend_views.add_book, name='add-book'),
    path('books/<int:pk>/delete/', frontend_views.delete_book_view, name='delete_book'),
    path('books/<int:pk>/update/', frontend_views.update_book_view, name='update_book'),



]