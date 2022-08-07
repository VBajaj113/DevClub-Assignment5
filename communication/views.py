from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


@login_required
def add_announcement(request, course_title):
    if not request.user.is_instructor:
        messages.success(request, f'Nice Try, huh!')
        return redirect('https://tinyurl.com/3wcyvb7x')
        
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.cleaned_data.get('announcement')
            title = form.cleaned_data.get('title')
            req = form.save(commit=False)
            req.course = Courses.objects.get(course_code=course_title)
            req.title = title
            req.announcement = announcement
            req.save()
            messages.success(request, f'The announcement has been sent to all students!')
            return redirect('home')
        
        context = {
            'title':'Announcement',
            'course_title':course_title,
            'form': form
        }

    else:
        form = AnnouncementForm()

        context = {
            'title':'Announcement',
            'course_title':course_title,
            'form': form
        }

    return render(request, 'communication/add_announcement.html', context)


@login_required
def announcement(request, course_title, announcement_title):
    context = {
        'title':'Announcement',
        'course_title':course_title,
        'announcement_title':announcement_title,
    }
    return render(request,'communication/announcement.html', context)


@login_required
def EditAnnouncement(request):
    if request.method == 'POST':
        form = EditAnnouncementForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data.get('course')
            old_title = form.cleaned_data.get('old_title')
            req = course.announcements_set.get(title=old_title)
            req.title = form.cleaned_data.get('title')
            req.announcement = form.cleaned_data.get('announcement')
            req.save()
            messages.success(request, f'Announcement has been edited!')
            return redirect('edit_announcement')
            
    else:
        form = EditAnnouncementForm()
    return render(request,'communication/edit_announcement.html', {'form':form})


@login_required
def message(request):
    context = {
        'title':'Message',
        'form':MessageForm(),
    }
    return render(request, 'communication/message.html', context)