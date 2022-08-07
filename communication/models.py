from django.db import models
from users.models import Courses, User


class Announcements(models.Model):
    title = models.CharField(max_length=255, default='', unique=True)
    announcement = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.course.course_code} : {self.title}'


class Messages(models.Model):
    message = models.TextField()
    send_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_to')
    send_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_from')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)