
### 2. Documenting `update.md`

**Open `update.md`** and include the following content:

```markdown
# update.md

## Update a Book Instance

To update the title of the book we created, access the instance and modify the title.

### Command
```python
book = Book.objects.get(title="1984")  # Retrieve the book instance first
book.title = "Nineteen Eighty-Four"
book.save()
