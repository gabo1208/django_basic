from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Quiniela, Game, GameResult


class QuinielaForm(forms.ModelForm):

    class Meta:
        model = Quiniela
        exclude = ('members', 'admin', 'tags')


class GameResultForm(forms.ModelForm):

    class Meta:
        model = GameResult
        exclude = ('game', 'user')


class BlockedGameResultForm(forms.ModelForm):

    class Meta:
        model = GameResult
        exclude = ('game', 'user')
        readonly_fields = ('score_home', 'score_away')

    def __init__(self, *args, **kwargs):
        super(BlockedGameResultForm, self).__init__(*args, **kwargs)
        self.fields['score_home'].widget.attrs['readonly'] = True
        self.fields['score_away'].widget.attrs['readonly'] = True


class InviteUsersForm(forms.Form):
    users = forms.CharField(max_length=50)