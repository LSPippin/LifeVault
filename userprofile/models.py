# userprofile/models.py
# Defines the UserProfile model which extends Django's built-in User model.
# Each user has exactly one profile stored via a OneToOneField relationship.
# The profile stores personal contact and identification information.

from django.db import models
from django.contrib.auth.models import User


# Extends the built-in Django User model with additional personal information.
# OneToOneField ensures each user can only have one profile.
# The profile is automatically created when first accessed using get_or_create.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One profile per user

    # Contact information
    phone = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    # Government identification — stored securely and only visible to the account owner
    social_security = models.CharField(max_length=11, blank=True)
    passport_number = models.CharField(max_length=20, blank=True)
    drivers_license = models.CharField(max_length=20, blank=True)
    tsa_precheck = models.CharField(max_length=20, blank=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
