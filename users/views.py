from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from PIL import Image


def register(request):
    return render(request, "users/register.html", {'title':'Registration'})


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

    return render(request, "users/StudentRegistration.html", {'user_form':user_form, 'student_form':student_form, 'title':'Student Registration'})


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

    return render(request, "users/InstructorRegistration.html", {'user_form':user_form, 'instructor_form':instructor_form, 'title':'Instructor Registration'})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserProfileForm(request.POST, instance=request.user)
        if request.user.is_student:
            p_form = StudentProfileForm(request.POST, request.FILES, instance=request.user.student_profile)
        else:
            p_form = InstructorProfileForm(request.POST, request.FILES, instance=request.user.instructor_profile)
        
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            password = u_form.cleaned_data.get('password')
            user.username = user.email.split('@')[0]
            user.first_name = user.name.split()[0]
            user.last_name = user.name.split()[-1]
            user.set_password(password)
            try:
                user.avatar = request.FILES['avatar']
                user.save()
                img = Image.open(user.avatar.path)
                img.thumbnail((300,300))
                img.save(user.avatar.path)
            except:
                user.save()
            
            
            if request.user.is_student:
                studentprofile = p_form.save(commit=False)
                studentprofile.user = user
                studentprofile.save()
            else:
                instructorprofile = p_form.save(commit=False)
                instructorprofile.user = user
                instructorprofile.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserProfileForm(instance=request.user)
        if request.user.is_student:
            p_form = StudentProfileForm(instance=request.user.student_profile)
        else:
            p_form = InstructorProfileForm(instance=request.user.instructor_profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
        'title':'Profile',
    }
    return render(request, 'users/profile.html', context)


@login_required
def homepage(request):
    return render(request, 'users/home.html')


def about(request):
    return render(request, 'users/about.html')