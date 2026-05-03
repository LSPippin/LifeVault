# vault/models.py
# Defines the core data models for LifeVault's generic record system.
# Categories organize records by life area. Records store individual
# entries within a category. Tags can be used for additional labeling.

from django.db import models
from django.contrib.auth.models import User


# Represents a life category such as Health, Insurance, or Home & Maintenance.
# Each category belongs to a specific user and has a slug for URL routing.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User-specific categories
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)  # URL-friendly version of the name e.g. 'home-maintenance'
    icon = models.CharField(max_length=10, default='📁')  # Emoji icon displayed in the UI

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


# Represents a single record entry within a category.
# Records support notes, document uploads, and optional reminder dates.
class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensures users only see their own records
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Which category this record belongs to
    title = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)  # Optional file attachment
    reminder_date = models.DateField(blank=True, null=True)  # Triggers dashboard alert when date arrives
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on every save

    def __str__(self):
        return self.title


# Optional labels that can be attached to records for additional organization
class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
