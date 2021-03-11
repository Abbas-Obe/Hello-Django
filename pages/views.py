from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Welcome to my blog")

def home(request):
    return HttpResponse("Welcome to the home page")

def ourPost(request):
    return HttpResponse("this is a post of abbas")
  
# Create your views here.
