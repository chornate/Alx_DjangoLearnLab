# delete.md

## Delete a Book Instance

To delete the book instance, you need to first import the `Book` model and then use the `delete()` method.

### Command
```python
from bookshelf.models import Book  # Import the Book model
book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the updated book instance
book.delete()  # Delete the book instance
