from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]
        
    def __str__(self):
        return self.title

# Automatically create a UserProfile when a new user is created
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class Author(models.Model):
    name = models.CharField(max_length=200)
    # Optionally, add other fields like birthdate, biography, etc.
    
    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100, blank=True, null=True)
    # Reference to Librarian: Assuming a librarian manages the book
    librarian = models.ForeignKey('Librarian', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can edit book'),
            ('can_delete_book', 'Can delete book')
        ]

# Librarian Model
class Librarian(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    library_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Librarian {self.user.username} at {self.library_name}"
