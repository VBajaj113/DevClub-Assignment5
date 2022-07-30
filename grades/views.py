from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


@login_required
def coursepage(request, course_title):
    return render(request, 'grades/coursepage.html', {'title':course_title})


@login_required
def studentsgrades(request, course_title):
    return render(request, 'grades/students_grades.html', {'title':course_title})


@login_required
def EditGradesRequest(request):
    if request.method == 'POST':
        form = EditGradesForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data.get('student')
            exam = form.cleaned_data.get('exam')
            req = student.studentgrade_set.get(exam=exam)
            req.marks_obtained = form.cleaned_data.get('marks_obtained')
            req.grade = form.cleaned_data.get('grade')
            req.save()
            messages.success(request, f'Grade for {student} has been changed!')
            return redirect('edit_grades')
            
    else:
        form = EditGradesForm()
    return render(request, 'grades/edit_grades.html', {'form':form})