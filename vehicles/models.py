from django.db import models
from django.contrib.auth.models import User


class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    vin = models.CharField(max_length=17, blank=True)
    purchase_date = models.DateField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to='vehicles/photos/', blank=True, null=True)
    registration_expiry = models.DateField(blank=True, null=True)
    insurance_provider = models.CharField(max_length=100, blank=True)
    insurance_policy = models.CharField(max_length=100, blank=True)
    insurance_expiry = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class VehicleMaintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True)
    document = models.FileField(upload_to='vehicles/maintenance/', blank=True, null=True)

    def __str__(self):
        return f"{self.vehicle} - {self.description}"


class OilChange(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    mileage = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    next_due_mileage = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.vehicle} - Oil Change {self.date}"

