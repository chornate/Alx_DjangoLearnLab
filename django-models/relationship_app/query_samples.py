from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None  # Handle case where the author doesn't exist

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    # Retrieve the library object
    library = Library.objects.get(name=library_name)
    # Use the OneToOne relationship to get the librarian for the library
    librarian = Librarian.objects.get(library=library)
    return librarian
