from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, "GUI/homepage.html", context={})

def template(request):
    return render(request, 'base.html', context = {})