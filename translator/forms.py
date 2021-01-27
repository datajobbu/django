from django import forms
from translator.models import FileUpload, FileDownload


class UploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['up_file']


class DownloadForm(forms.ModelForm):
    class Meta:
        model = FileDownload
        fields = ['dw_file']