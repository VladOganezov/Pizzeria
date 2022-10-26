from .models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(label="Email", widget=forms.EmailInput)
    username = forms.CharField(label="Enter your first name", widget=forms.TextInput)
    password = forms.CharField(label="Password:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat your Password:", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords didn't match!")
        return data['password2']


class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


