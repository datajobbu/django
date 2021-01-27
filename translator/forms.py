from django import forms
from translator.models import FileUpload


class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['up_file']
