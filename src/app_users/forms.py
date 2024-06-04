
from django.forms import ModelForm
from django import forms
from .models import Profile

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'displayName', 'info']
        widgets = {
            'image': forms.FileInput(),
            'displayName': forms.TextInput(attrs={'placeholder': 'Display name'}),
            'info': forms.Textarea(attrs={'placeholder': 'Information about yourself'}),
        }
