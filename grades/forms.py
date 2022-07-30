from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from .models import *


class EditGradesForm(ModelForm):
    class Meta:
        model = StudentGrade
        fields = '__all__'