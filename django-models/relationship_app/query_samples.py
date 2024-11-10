from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author using objects.filter
def get_books_by_author(author_name):
    # First, retrieve the author
    author = Author.objects.get(name=author_name)
    # Use filter to get all books related to the author
    return Book.objects.filter(author=author)

# List all books in a library
def get_books_in_library(library_name):
    # Retrieve the library
    library = Library.objects.get(name=library_name)
    # Return all books in the library
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    # Retrieve the library
    library = Library.objects.get(name=library_name)
    # Return the librarian assigned to the library
    return library.librarian