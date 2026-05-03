from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    microchip_number = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='pets/photos/', blank=True, null=True)
    breeder_name = models.CharField(max_length=100, blank=True)
    breeder_phone = models.CharField(max_length=20, blank=True)
    breeder_email = models.EmailField(blank=True)
    vet_name = models.CharField(max_length=100, blank=True)
    vet_phone = models.CharField(max_length=20, blank=True)
    vet_email = models.EmailField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PetAppointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pet.name} - {self.title}"


class PetMedication(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100, blank=True)
    frequency = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pet.name} - {self.name}"


class PetVaccine(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_given = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    administered_by = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='pets/vaccines/', blank=True, null=True)

    def __str__(self):
        return f"{self.pet.name} - {self.name}"
