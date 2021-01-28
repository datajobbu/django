import os

from uuid import uuid4
from datetime import datetime

from django.db import models
from django.conf import settings
#from django.utils import timezone


class CSVUpload(models.Model):
    tid = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    sum_amt_1d = models.CharField(max_length=30)
    sum_cnt_1d = models.CharField(max_length=5)
    cnt_opp_1d = models.CharField(max_length=5)
    aml_code = models.CharField(max_length=10)
    code_name = models.CharField(max_length=50)
    report_date = models.CharField(max_length=20)

    def __str__(self):
        return self.tid