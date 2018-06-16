from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Quiniela, Game, GameResult, OscarCoin


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

    def get_winner(self):
        return self.instance.get_winner()


class InviteUsersForm(forms.Form):
    users = forms.CharField(max_length=50)


class OscarCoinForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': _("The Secret Phrase is not correct."),
    }
    secret_phrase = forms.CharField(label=_("Secret Phrase"), widget=forms.PasswordInput)

    class Meta:
        model = OscarCoin
        fields = ['value', 'secret_phrase']

    def clean_secret_phrase(self):
        phrase = self.cleaned_data.get("secret_phrase")
        if phrase and phrase != "merwebochico":
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return phrase