from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def coursepage(request, course_title):
    return render(request, 'grades/coursepage.html', {'title':course_title})


@login_required
def studentsgrades(request, course_title):
    return render(request, 'grades/students_grades.html', {'title':course_title})