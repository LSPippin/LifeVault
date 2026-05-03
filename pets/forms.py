from django import forms
from .models import Pet, PetAppointment, PetMedication, PetVaccine


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name', 'species', 'breed', 'date_of_birth',
            'microchip_number', 'photo',
            'breeder_name', 'breeder_phone', 'breeder_email',
            'vet_name', 'vet_phone', 'vet_email', 'notes'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Pet name'}),
            'species': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Dog, Cat'}),
            'breed': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Breed'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'microchip_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Microchip number'}),
            'breeder_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Breeder name'}),
            'breeder_phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Breeder phone'}),
            'breeder_email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Breeder email'}),
            'vet_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Vet name'}),
            'vet_phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Vet phone'}),
            'vet_email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Vet email'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Additional notes'}),
        }


class PetAppointmentForm(forms.ModelForm):
    class Meta:
        model = PetAppointment
        fields = ['title', 'date', 'location', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Appointment title'}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Location'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Notes'}),
        }


class PetMedicationForm(forms.ModelForm):
    class Meta:
        model = PetMedication
        fields = ['name', 'dosage', 'frequency', 'start_date', 'end_date', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Medication name'}),
            'dosage': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 10mg'}),
            'frequency': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Once daily'}),
            'start_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Notes'}),
        }


class PetVaccineForm(forms.ModelForm):
    class Meta:
        model = PetVaccine
        fields = ['name', 'date_given', 'expiry_date', 'administered_by', 'document']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Vaccine name'}),
            'date_given': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'administered_by': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Administered by'}),
        }
