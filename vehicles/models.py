# vehicles/models.py
# Defines the data models for the Vehicles module.
# Each vehicle belongs to a user and can have related maintenance
# records and oil change history stored as separate models.

from django.db import models
from django.contrib.auth.models import User


# Main vehicle profile — stores all core information about a single vehicle
class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links vehicle to its owner
    make = models.CharField(max_length=100)  # e.g. Toyota, Jeep
    model = models.CharField(max_length=100)  # e.g. Camry, Grand Cherokee
    year = models.CharField(max_length=4)  # e.g. 2020
    vin = models.CharField(max_length=17, blank=True)  # Vehicle Identification Number
    purchase_date = models.DateField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to='vehicles/photos/', blank=True, null=True)

    # Registration information
    registration_expiry = models.DateField(blank=True, null=True)  # Tracks when registration needs renewal

    # Insurance information
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_policy = models.CharField(max_length=100, blank=True)
    insurance_expiry = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set automatically on creation

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


# Stores individual maintenance records linked to a specific vehicle
# Supports document upload for storing receipts or service reports
class VehicleMaintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Deletes records if vehicle is deleted
    description = models.CharField(max_length=200)  # e.g. Brake replacement, Tire rotation
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)  # Shop name or location
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True)
    document = models.FileField(upload_to='vehicles/maintenance/', blank=True, null=True)  # Optional receipt upload

    def __str__(self):
        return f"{self.vehicle} - {self.description}"


# Stores oil change history for a specific vehicle
# Tracks mileage to help users know when the next oil change is due
class OilChange(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    mileage = models.IntegerField(blank=True, null=True)  # Mileage at time of oil change
    location = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    next_due_mileage = models.IntegerField(blank=True, null=True)  # Mileage when next oil change is due
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.vehicle} - Oil Change {self.date}"
