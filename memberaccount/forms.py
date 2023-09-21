from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    username = forms.CharField(max_length=150, label=False)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None

        self.fields['username'].widget.attrs.update({
            'class': 'form-control mb-3',
            'type': 'username',
            'name': 'username',
            'id': 'username',
            'required': '',
            'placeholder': '',
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control mb-3',
            'type': 'password',
            'name': 'password1',
            'id': 'password1',
            'required': '',
            'placeholder': '',
        })
