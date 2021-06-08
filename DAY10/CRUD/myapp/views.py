from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Driver 
from .models import Constructor

def homepageview(request):
    return render(request,'home.html')

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')

class driverlist(ListView):
    model = Driver
    template_name = 'dlist.html'

class constructorlist(ListView):
    model = Constructor
    template_name = 'clist.html'