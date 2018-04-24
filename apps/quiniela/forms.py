from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Quiniela


class QuinielaForm(forms.ModelForm):

    class Meta:
        model = Quiniela
        exclude = ('members',)
