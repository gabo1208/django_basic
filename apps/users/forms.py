from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.translation import ugettext, ugettext_lazy as _

from .models import Profile, User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'country', 'city',
            'location', 'phone',
            'mail', 'image',
            'description', 'interests',
        ]

class UserCreationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification.")
    )

    class Meta:
        model = User
        fields = [
            'email', 'username',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user

class UserLoginForm(forms.Form):
    username = forms.CharField(label=_("Username/Email"),
                               max_length=25,
                               required=True)
    password = forms.CharField(label=_("Password"),
                               strip=False,
                               widget=forms.PasswordInput,
                               required=True)

    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                self.user_cache = authenticate(username=username, password=password)
            else:
                user = User.objects.filter(email=username)
                if user.exists():
                	self.user_cache = authenticate(username=user[0].username, password=password)
                else:
                	self.user_cache = None

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': 'username/email'},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',

            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class CustomPasswordResetForm(PasswordResetForm):

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
            Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, 'admin@memberit.com', [to_email])
        # New line introduce
        email_message.attach_alternative(body, 'text/html')

        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()
