from django.urls import path
from . import views

app_name = 'translator'

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
]
