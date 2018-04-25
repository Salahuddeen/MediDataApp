from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^base', views.template, name='template'),
    path('patientCatalog/', views.patientCatalog.as_view(), name='patientCatalog'),
    path('book/<int:pk>', views.patientDetail.as_view(),name='patientDetails'),

    url(r'^patients', views.viewAllPatients, name='patients'),
    url(r'^', views.homepage, name='__homepage'),
]