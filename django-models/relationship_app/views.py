from django.shortcuts import render
from django.http import HttpResponse
from .models import Library
from .models import Book  # Import both Book and Library models
from django.views.generic.detail import DetailView

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specify the model for the DetailView
    template_name = 'relationship_app/library_detail.html'  # Define the template to be used
    context_object_name = 'library'  # The object will be accessible as 'library' in the template
