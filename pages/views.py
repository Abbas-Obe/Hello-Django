from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name="home.html"

class CreatePageView(TemplateView):
    template_name="about.html"    


def homePageView(request):
    return HttpResponse("Welcome to my blog")

  
# Create your views here.
