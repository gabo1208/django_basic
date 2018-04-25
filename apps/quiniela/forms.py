from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Quiniela, Game, GameResult


class QuinielaForm(forms.ModelForm):

    class Meta:
        model = Quiniela
        exclude = ('members',)

class GameResultForm(forms.ModelForm):

    class Meta:
        model = GameResult
        exclude = ('game', 'user')