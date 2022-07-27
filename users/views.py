from django.shortcuts import redirect, render
from .models import StudentProfile, InstructorProfile, User
from .forms import *
from django.contrib import messages


def register(request):
    return render(request, "users/register.html")


def StudentSignUp(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentProfileForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            user.is_student = True
            user.username = user.email.split('@')[0]
            user.first_name = user.name.split()[0]
            user.last_name = user.name.split()[-1]
            user.set_password(password)
            user.save()

            studentprofile = student_form.save(commit=False)
            studentprofile.user = user
            studentprofile.save()
            name = user_form.cleaned_data.get('name')
            messages.success(request, f'Account created for {name}! Please LogIn to continue.')
            return redirect('login')

    else:
        user_form = UserForm()
        student_form = StudentProfileForm()

    return render(request, "users/StudentRegistration.html", {'user_form':user_form, 'student_form':student_form})


def InstructorSignUp(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        instructor_form = InstructorProfileForm(request.POST)

        if user_form.is_valid() and instructor_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            user.is_instructor = True
            user.username = user.email.split('@')[0]
            user.first_name = user.name.split()[0]
            user.last_name = user.name.split()[-1]
            user.set_password(password)
            user.save()

            instructorprofile = instructor_form.save(commit=False)
            instructorprofile.user = user
            instructorprofile.save()

            name = user_form.cleaned_data.get('name')
            messages.success(request, f'Account created for {name}! Please LogIn to continue.')
            return redirect('login')

    else:
        user_form = UserForm()
        instructor_form = InstructorProfileForm()

    return render(request, "users/InstructorRegistration.html", {'user_form':user_form, 'instructor_form':instructor_form})


#profile