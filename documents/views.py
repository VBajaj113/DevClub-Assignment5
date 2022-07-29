from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import DocumentsForm


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