from django.urls import path
from django.conf.urls import url
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('profile/<username>/', views.profile, name='profile'),
    
]