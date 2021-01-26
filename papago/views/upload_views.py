from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..forms import UploadForm
from ..models import FileUpload


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('Success!')
    
    else:
        form = UploadForm()
    
    return render(request, 'papago/upload_form.html', {'form': form})