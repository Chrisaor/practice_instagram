from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
app_name = 'instagram'
urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name = 'index'),
    path('upload/', views.upload, name='upload')
]
