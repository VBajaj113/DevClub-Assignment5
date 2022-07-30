from django.forms import ModelForm
from .models import *


class EditGradesForm(ModelForm):
    class Meta:
        model = StudentGrade
        fields = '__all__'