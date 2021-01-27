import os

from uuid import uuid4
from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone


def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex

    return '/'.join(['upload_file/', ymd_path, uuid_name])


class FileUpload(models.Model):
    up_file = models.FileField(null=True, blank=True, verbose_name='file')
    #filename = models.CharField(max_length=64, null=True, verbose_name='filename')