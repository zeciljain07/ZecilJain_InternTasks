from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("Hello World!!")
