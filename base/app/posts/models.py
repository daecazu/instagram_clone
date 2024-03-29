"""Posts models"""

# Django
from django.db import models

# models
from core.models import User

class Post(models.Model):
    """Post model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and user name"""
        return f"{self.title} by @{self.user.username}"    