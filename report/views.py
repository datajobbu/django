import os
import csv
import urllib
import mimetypes

from pathlib import Path

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from config import settings
from .forms import CSVForm
from .models import CSVUpload


def index(request):
	return render(request, 'report/report.html')


def csv_upload(request):
    """ CSV 파일 읽기 """
    path = settings.AML_ROOT +'/' + "t1.csv"
    aml_list = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            tid=row[0]
            age=row[1]
            gender=row[2]
            sum_amt_1d=row[3]
            sum_cnt_1d=row[4]
            cnt_opp_1d=row[5]
            aml_code=row[6]
            code_name=row[7]
            report_date=row[8]
            break

    return render(request, 'report/report.html', {'tid':tid, 'age':age, 'gender':gender, 'report_date':report_date,
                                                  'sum_amt_1d':sum_amt_1d, 'sum_cnt_1d':sum_cnt_1d, 'cnt_opp_1d':cnt_opp_1d,
                                                  'aml_code':aml_code, 'code_name':code_name})
