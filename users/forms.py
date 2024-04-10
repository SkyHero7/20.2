from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class VerificationForm(forms.Form):
    email = forms.EmailField()
    verification_code = forms.CharField(max_length=6, min_length=6, widget=forms.TextInput(attrs={'maxlength': '6', 'minlength': '6'}))