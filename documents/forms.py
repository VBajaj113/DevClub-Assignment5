from django import forms
from .models import Documents


class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields=['name','date','course','doc']


class EditDocumentsForm(forms.ModelForm):
    old_name = forms.CharField(max_length=255)

    class Meta:
        model = Documents
        fields = ['old_name', 'name','date','course','doc']
    
    def clean(self):
        cleaned_data = super(EditDocumentsForm, self).clean()
        old_name = cleaned_data.get("old_name")
        course = cleaned_data.get('course')

        if old_name not in [i.name for i in course.documents_set.all()]:
            self.add_error('old_name', "No document of this name has been uploaded.")

        return cleaned_data