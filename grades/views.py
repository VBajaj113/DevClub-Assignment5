from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def coursepage(request, course_title):
    return render(request, 'grades/coursepage.html', {'title':course_title})