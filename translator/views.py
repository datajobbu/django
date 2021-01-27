from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from .forms import UploadForm
from .models import FileUpload
from .translate import translate_papago

# Create your views here.
def file_upload(request):
    form = UploadForm()
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                translate_papago(request.FILES['up_file'].name)
            except:
                None
            #print(request.FILES['up_file'].name)

    return render(request, 'translator/upload_form.html', {'form':form})
