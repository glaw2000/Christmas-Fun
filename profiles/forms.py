from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'first_name', 'last_name']
        widgets = {
            'created_on': forms.TextInput(attrs={'readonly': 'readonly'}),
            'last_login': forms.TextInput(attrs={'readonly': 'readonly'}),
        }