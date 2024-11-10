from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    # Use get to retrieve the Author object, or handle the case where the author doesn't exist
    try:
        author = Author.objects.get(name=author_name)
        # Filter books by the retrieved author
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None  # Handle case where the author doesn't exist

# List all books in a library
def get_books_in_library(library_name):
    # Retrieve the library by name
    library = Library.objects.get(name=library_name)
    # Return all books in the library
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    # Retrieve the library
    library = Library.objects.get(name=library_name)
    # Return the librarian assigned to the library
    return library.librarian
