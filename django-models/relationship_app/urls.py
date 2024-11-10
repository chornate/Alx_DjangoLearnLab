from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import list_books

urlpatterns = [
    path('add/', views.add_book, name='add_book'),  # Add book view
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit book view
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete book view
    path('books/', views.list_books, name='list_books'), 
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    # Built-in login view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Built-in logout view
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Custom registration view
    path('register/', views.register, name='register'),

    # Function-based view for listing books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for displaying library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
