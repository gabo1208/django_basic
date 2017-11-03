from django import forms

from .models import *


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'country', 'city',
            'location', 'phone',
            'mail', 'image',
            'description', 'interests',
        ]
