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
            user_form.save()
            student_form.save()
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
            user_form.save()
            instructor_form.save()
            name = user_form.cleaned_data.get('name')
            messages.success(request, f'Your account has been created! Please LogIn to continue.')
            return redirect('login')

    else:
        user_form = UserForm()
        instructor_form = InstructorProfileForm()

    return render(request, "users/InstructorRegistration.html", {'user_form':user_form, 'instructor_form':instructor_form})


#profile