from django.contrib import admin
from django.urls import path
from . import views
app_name = 'instagram'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('upload/', views.upload, name='upload')
]
