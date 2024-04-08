from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.submit, name='submit'),
    path('download', views.download_excel, name='download'),
]
