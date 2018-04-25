from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .customModels import (
    Ailments,
    Doctor,
    Hospital,
    OTCMedicine,
    Patient,
    Treatment,
    Appointment,
    OTCMeds,
    patientIllness,
)


# Create your views here.
def homepage(request):
    return render(request, "GUI/homepage.html", context={})

def template(request):
    return render(request, 'base.html', context = {})

def viewAllPatients(request):
    patientInfo = Patient.objects.all()
    context = { 'patient': patientInfo }
    return render(request,'GUI/patientInfo.html', context)

def viewAllDoctors(request):
    return render(request, 'patientInfo.html', context ={})

def resetPatientCode(request):
    return render (request, 'patientInfo.html', context ={})

def viewAllHospitals(request):
    return render(request, 'patientInfo.html', context={})

class patientCatalog(generic.View):
    model = Patient
    context_object_name = 'patient_catalog'
    template_name = 'GUI/patientCatalog.html'

class patientDetail(generic.DetailView):
    model=Patient
    context_object_name = 'patientDetail'
    template_name = 'GUI/patientDetail.html'