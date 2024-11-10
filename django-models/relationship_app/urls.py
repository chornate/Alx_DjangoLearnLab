from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
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
