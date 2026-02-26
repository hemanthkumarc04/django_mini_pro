from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'category', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'What needs to be done?',
                'autocomplete': 'off',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input form-textarea',
                'placeholder': 'Add some details...',
                'rows': 4,
            }),
            'status': forms.Select(attrs={'class': 'form-input form-select'}),
            'priority': forms.Select(attrs={'class': 'form-input form-select'}),
            'category': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Work, Personal, Health',
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
        }
