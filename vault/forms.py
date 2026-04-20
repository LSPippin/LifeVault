from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'notes', 'document', 'reminder_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Record title',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Add any notes here...',
                'rows': 4,
            }),
            'reminder_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
        }
