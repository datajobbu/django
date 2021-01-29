from . import views
from django.urls import path

app_name = "report"

urlpatterns = [
	path('', views.index, name='index'),
	path('<str:tid>/', views.detail, name='detail'),
]