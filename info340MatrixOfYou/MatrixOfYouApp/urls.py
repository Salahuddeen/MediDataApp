from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^base', views.template, name='homepage'),
    url(r'^', views.homepage, name='__homepage'),
]