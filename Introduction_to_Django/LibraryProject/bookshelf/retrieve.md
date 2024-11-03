# retrieve.md

## Retrieve a Book Instance

To retrieve and display all attributes of the book instance you created, use the `get()` method.

### Command
```python
book = Book.objects.get(title="1984")  # Retrieve the book instance by title
print(book.title, book.author, book.publication_year)
