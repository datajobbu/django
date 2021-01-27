import os
import urllib
import mimetypes

from pathlib import Path
from pptx import Presentation

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from config import settings
from .forms import UploadForm
from .models import FileUpload

from .papago_api import translate_ppt


def file_upload(request):
    """ 번역할 파일 업로드 """
    form = UploadForm()
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                name = request.FILES['up_file'].name
                translate_papago(name)

                return render(request, 'translator/download_form.html', {'name':name})

            except:
                None

    return render(request, 'translator/upload_form.html', {'form':form})


def file_download(request, filename):
    """ 번역된 파일 다운로드 """
    file_name = 'translated_' + filename
    file_url = settings.MEDIA_ROOT +'/' + file_name
    
    if request.method == 'GET':
        if os.path.exists(file_url):
            with open(file_url, 'rb') as fh:
                quote_file_url = urllib.parse.quote(file_name.encode('utf-8'))
                response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
                response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
                return response
            raise Http404

    return render(request, 'translator/download_form.html')


def translate_papago(filename):
    """ 파파고 API 이용 번역 """
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = os.path.join(BASE_DIR, 'media/')
    prs = Presentation(path + filename)

    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue

            for paragraph in shape.text_frame.paragraphs:
                translated = translate_ppt(paragraph.text)
                paragraph.clear()
                
                run = paragraph.add_run()
                run.text = translated

    prs.save(path + "translated_" + filename)