from django.shortcuts import render


def coursepage(request, course_title):
    return render(request, 'grades/coursepage.html', {'title':course_title})