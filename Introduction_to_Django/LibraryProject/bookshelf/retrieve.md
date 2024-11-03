# retrieve.md

## Retrieve a Book Instance

To retrieve all book instances from the database, you can use the `Book.objects.all()` method.

### Command
```python
retrieved_books = Book.objects.all()
print(retrieved_books)
