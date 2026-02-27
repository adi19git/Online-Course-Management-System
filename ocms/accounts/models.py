from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model for LMS
class User(AbstractUser):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )

    full_name = models.CharField(max_length=150)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username