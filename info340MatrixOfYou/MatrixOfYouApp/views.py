from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("Homepage")

def template(request):
    return render(request, 'base.html', context = {})