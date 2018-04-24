from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, "GUI/homepage.html", context={})

def template(request):
    return render(request, 'base.html', context = {})

def viewAllPatients(request):
    return render(request,'patientInfo.html', context = {})

def viewAllDoctors(request):
    return render(request, 'patientInfo.html', context ={})

def resetPatientCode(request):
    return render (request, 'patientInfo.html', context ={})

def viewAllHospitals(request):
    return render(request, 'patientInfo.html', context={})

