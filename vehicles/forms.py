from django import forms
from .models import Vehicle, VehicleMaintenance, OilChange


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'make', 'model', 'year', 'vin',
            'purchase_date', 'purchase_price', 'photo',
            'registration_expiry',
            'insurance_provider', 'insurance_policy', 'insurance_expiry',
            'notes'
        ]
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Toyota'}),
            'model': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Camry'}),
            'year': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 2020'}),
            'vin': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'VIN number'}),
            'purchase_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '0.00'}),
            'registration_expiry': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'insurance_provider': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Insurance provider'}),
            'insurance_policy': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Policy number'}),
            'insurance_expiry': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class VehicleMaintenanceForm(forms.ModelForm):
    class Meta:
        model = VehicleMaintenance
        fields = ['description', 'date', 'location', 'price', 'notes', 'document']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Brake replacement'}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Shop name or location'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '0.00'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class OilChangeForm(forms.ModelForm):
    class Meta:
        model = OilChange
        fields = ['date', 'mileage', 'location', 'price', 'next_due_mileage', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'mileage': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Current mileage'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Shop name or location'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': '0.00'}),
            'next_due_mileage': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Next due mileage'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }
