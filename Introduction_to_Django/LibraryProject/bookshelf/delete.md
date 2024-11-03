
### 3. Documenting `delete.md`

**Open `delete.md`** and add the following content:

```markdown
# delete.md

## Delete a Book Instance

To delete the book instance, you can use the `delete()` method.

### Command
```python
book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the updated book instance
book.delete()
