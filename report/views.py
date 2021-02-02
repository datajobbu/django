import os
import csv
import urllib
import mimetypes
import xhtml2pdf.pisa as pisa

from io import BytesIO
from pathlib import Path

from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404

from config import settings
from .models import CSVUpload


def index(request):
    """
    initial: csv 읽기(수정 필요## PostgreSQL과 연동할 예정) 
    input: request
    return: aml 테이블 html
    """
    '''
    path = settings.AML_ROOT +'/' + "t1.csv"
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            CSVUpload.objects.create(tid=row[0], age=row[1], gender=row[2], sum_amt_1d=row[3],
                                     sum_cnt_1d=row[4], cnt_opp_1d=row[5], aml_code=row[6],
                                     code_name=row[7], report_date=row[8])
    '''
    aml_list = CSVUpload.objects.order_by('-report_date')
    return render(request, 'report/report.html', {'aml_list':aml_list})

'''
def detail(request, tid):
    """ AML 상세 정보 html 반환 """
    aml_list = CSVUpload.objects.filter(tid=tid).values()
    context = {'aml_list' : aml_list}
    return render(request, 'report/report_detail.html', context)
'''
 
def detail(request, tid):
    """ AML 상세 정보를 PDF로 반환(영어만 가능## 수정 예정) """
    aml_list = CSVUpload.objects.filter(tid=tid).values()
    context = {'aml_list' : aml_list}

    template = get_template('report/pdf.html')
    html = template.render(context)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)

    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')

    else:
        return HttpResponse("Error Rendering PDF", status=400)
    
    return render(request, 'report/pdf.html', context)