# create.md

## Create a Book Instance

To create a new instance of the `Book` model, you can use the `Book.objects.create` method.

### Command
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
