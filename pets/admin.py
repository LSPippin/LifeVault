from django.contrib import admin
from .models import Pet, PetAppointment, PetMedication, PetVaccine

admin.site.register(Pet)
admin.site.register(PetAppointment)
admin.site.register(PetMedication)
admin.site.register(PetVaccine)
