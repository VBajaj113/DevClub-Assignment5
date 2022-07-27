from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib import admin
from .models import *

admin.site.register(Departments)
admin.site.register(Programme)
admin.site.register(Courses)
admin.site.register(StudentProfile)
admin.site.register(InstructorProfile)


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    fieldsets = UserAdmin.fieldsets
    fieldsets += (
        ('Custom',{
            'fields':('avatar', 'department', 'is_student', 'is_instructor')
        }),
    ) 

admin.site.register(User, MyUserAdmin)