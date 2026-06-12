from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Car


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["make", "model", "year", "color", "price", "registration_number"]

    def clean_year(self):
        year = self.cleaned_data["year"]
        max_year = date.today().year + 1
        if year < 1886 or year > max_year:
            raise forms.ValidationError(f"Year must be between 1886 and {max_year}.")
        return year

    def clean_registration_number(self):
        return self.cleaned_data["registration_number"].strip().upper()
