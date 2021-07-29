"""users forms"""

# Django
from django import forms


class ProfileForm(forms.Form):
    """user Form"""
    website = forms.URLField(max_length=255, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()