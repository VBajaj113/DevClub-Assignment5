from django.db import models
from users.models import Courses


class Documents(models.Model):
    name = models.CharField(max_length=255, null=True, default='')
    date = models.DateField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)
    doc = models.FileField(upload_to='documents')

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return f'{self.course} : {self.name}'