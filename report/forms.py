from django import forms
from report.models import CSVUpload


class CSVForm(forms.ModelForm):
    class Meta:
        model = CSVUpload
        fields = ['tid']