from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from PIL import Image


class Departments(models.Model):
    name = models.CharField(max_length=100, null=True, default="", unique=True)
    department_code = models.CharField(max_length=5, null=True, default="", unique=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class Programme(models.Model):
    name = models.CharField(max_length=100, null=True, default="")
    department = models.ForeignKey(Departments, null=True, on_delete=models.CASCADE)
    programme_code = models.CharField(max_length=5, null=True, default="")

    class Meta:
        verbose_name = 'Programme'
        verbose_name_plural = 'Programmes'

    def __str__(self):
        return self.programme_code


class Courses(models.Model):
    name = models.CharField(max_length=100, null=True, default='')
    course_code = models.CharField(max_length=10, null=True, default='')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course_code


#-------------------------------------------------------------------------------------------


class User(AbstractUser):
    name = models.CharField(max_length=255, null=True, default='')
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    department = models.ForeignKey(Departments, null=True, on_delete=models.SET_NULL)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


class StudentProfile(models.Model):
    user = models.OneToOneField(
            User, 
            on_delete=models.CASCADE, 
            null=True,
            related_name='student_profile',
        )
    programme = models.ForeignKey(Programme, null=True, on_delete=models.SET_NULL)
    entry_num = models.CharField(max_length=11, null=True, verbose_name='Entry Number')
    kerberos_id = models.CharField(max_length=9, null=True, verbose_name='Kerberos ID')
    courses = models.ManyToManyField(Courses)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self):
        return self.user.name


class InstructorProfile(models.Model):
    user = models.OneToOneField(
            User, 
            on_delete=models.CASCADE, 
            null=True,
            related_name='instructor_profile',
        )
    is_head_of_department = models.BooleanField(default=False)
    courses = models.ManyToManyField(Courses)

    class Meta:
        verbose_name = 'Intructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return self.user.name


