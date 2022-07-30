from django.db import models
from users.models import *


class Exams(models.Model):
    course = models.ForeignKey(Courses, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, default='', unique=True)
    last_date = models.DateTimeField(verbose_name="Submission Deadline", blank=True, null=True)
    max_marks = models.PositiveIntegerField(default=100)

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

    def __str__(self):
        return f'{self.course.course_code} : {self.name}'


class StudentGrade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(decimal_places=2, max_digits=10)
    grade_choices =[
        ('A', 'A'),
        ('A-', 'A-'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D', 'D'),
        ('F', 'F'),
        ('I', 'I'),
    ]
    grade = models.CharField(max_length=2, choices=grade_choices, default='I')

    class Meta:
        verbose_name = "Student's Grade"
        verbose_name_plural = "Student's Grades"

    def __str__(self):
        return f'{self.student} : {self.exam}'