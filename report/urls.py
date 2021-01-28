from . import views
from django.urls import path

app_name = "report"

urlpatterns = [
	path('', views.csv_upload, name='index'),
]