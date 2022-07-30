from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *


def DocumentsUpload(request):
    if request.method == 'POST':
        form = DocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.doc = request.FILES['doc']
            doc.save()
            name = request.POST['name']
            messages.success(request, f'{name} has been uploaded!')
            return redirect('documents_upload')
    else:
        form = DocumentsForm()

    return render(request, 'documents/documents_upload.html', {'form':form})


def EditDocumentsRequest(request):
    if request.method == 'POST':
        form = EditDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            old_name = form.cleaned_data.get('old_name')
            new_name = form.cleaned_data.get('name')
            course = form.cleaned_data.get('course')
            doc = request.FILES['doc']
            date = form.cleaned_data.get('date')
            for i in course.documents_set.all():
                if i.name == old_name:
                    i.doc = doc
                    i.date = date
                    i.name = new_name
                    i.save()
                    break

            messages.success(request, f'{new_name} has been updated!')
            return redirect('edit_documents')
    else:
        form = EditDocumentsForm()

    return render(request, 'documents/edit_documents.html', {'form':form})