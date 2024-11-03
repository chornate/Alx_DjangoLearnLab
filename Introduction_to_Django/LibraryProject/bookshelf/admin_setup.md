# admin_setup.md

## Enhancing the Admin Interface for Book Model

### Step 1: Register the Book Model
In `bookshelf/admin.py`, register the `Book` model:
```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
