# pets/models.py
# Defines the data models for the Pets module.
# Each pet belongs to a user and can have related appointments,
# medications, and vaccine records stored as separate models.

from django.db import models
from django.contrib.auth.models import User


# Main pet profile — stores all core information about a single pet
class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links pet to its owner
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)  # e.g. Dog, Cat, Bird
    breed = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    microchip_number = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='pets/photos/', blank=True, null=True)

    # Breeder contact information
    breeder_name = models.CharField(max_length=100, blank=True)
    breeder_phone = models.CharField(max_length=20, blank=True)
    breeder_email = models.EmailField(blank=True)

    # Veterinarian contact information
    vet_name = models.CharField(max_length=100, blank=True)
    vet_phone = models.CharField(max_length=20, blank=True)
    vet_email = models.EmailField(blank=True)

    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set automatically on creation

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Alphabetical by default


# Stores individual vet appointments linked to a specific pet
class PetAppointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Deletes appointments if pet is deleted
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pet.name} - {self.title}"


# Stores medication records for a specific pet
class PetMedication(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100, blank=True)  # e.g. 10mg
    frequency = models.CharField(max_length=100, blank=True)  # e.g. Once daily
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pet.name} - {self.name}"


# Stores vaccine records for a specific pet
# Supports document upload for storing vaccine certificates
class PetVaccine(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_given = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    administered_by = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='pets/vaccines/', blank=True, null=True)  # Optional certificate upload

    def __str__(self):
        return f"{self.pet.name} - {self.name}"
