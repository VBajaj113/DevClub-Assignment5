from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from .models import *


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password', 'department']
    

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data


class StudentProfileForm(ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['programme', 'kerberos_id', 'courses']


class InstructorProfileForm(ModelForm):
    class Meta:
        model = InstructorProfile
        fields = ['courses', 'is_head_of_department']