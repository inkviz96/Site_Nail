from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', views.main_page, name='form_create_appointment'),
    path('index/', views.post, name='post'),
]
