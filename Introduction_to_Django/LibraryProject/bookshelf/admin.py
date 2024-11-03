from django.contrib import admin
from .models import Book  # Ensure this line is present

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Fields to include in the search
    list_filter = ('publication_year',)  # Enable filtering by publication year

# Register your models here.
admin.site.register(Book, BookAdmin)
