import os
import csv
import urllib
import mimetypes

from pathlib import Path

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from config import settings
from .forms import CSVForm
from .models import CSVUpload


def index(request):
    path = settings.AML_ROOT +'/' + "t1.csv"

    '''with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            CSVUpload.objects.create(tid=row[0], age=row[1], gender=row[2], sum_amt_1d=row[3],
                                     sum_cnt_1d=row[4], cnt_opp_1d=row[5], aml_code=row[6],
                                     code_name=row[7], report_date=row[8])'''
    
    aml_list = CSVUpload.objects.order_by('-report_date')

    return render(request, 'report/report.html', {'aml_list':aml_list})


def detail(request, tid):
    aml_list = CSVUpload.objects.filter(tid=tid).values()
    context = {'aml_list' : aml_list}
    #aml_list = CSVUpload.objects.filter(tid=tid)
    #aml_list.delete()

    return render(request, 'report/report_detail.html', context)
    
