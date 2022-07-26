from unicodedata import name
from django.contrib import admin
from .models import *

admin.site.register(Departments)
admin.site.register(Programme)
admin.site.register(Courses)
admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(InstructorProfile)
