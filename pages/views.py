from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Welcome to my blog")

  
# Create your views here.
