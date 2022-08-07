from django import forms
from django.forms import ModelForm
from .models import *


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'announcement']


class EditAnnouncementForm(ModelForm):
    old_title = forms.CharField(max_length=255)
    class Meta:
        model = Announcements
        fields = ['old_title', 'course', 'title', 'announcement']


class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['send_to', 'message']