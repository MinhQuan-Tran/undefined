from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ("individual", "Individual"),
        ("provider", "Provider"),
    )

    name = models.CharField(max_length=255)  # Set from Google name
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="individual")
    profile_picture = models.URLField(blank=True, null=True)  # Store Google profile image URL
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Rating between 1-5

    def __str__(self):
        return self.username  # You can also use `self.name` if you prefer
