from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email address'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone', 'street', 'city', 'state', 'zip_code',
            'social_security', 'passport_number',
            'drivers_license', 'tsa_precheck', 'notes'
        ]
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '(555) 555-5555'}),
            'street': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Street address'}),
            'city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Zip code'}),
            'social_security': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'XXX-XX-XXXX'}),
            'passport_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Passport number'}),
            'drivers_license': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'License number'}),
            'tsa_precheck': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'TSA PreCheck number'}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3, 'placeholder': 'Additional notes'}),
        }
