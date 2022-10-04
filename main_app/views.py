from unicodedata import name
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Youtuber

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Youtuberlist(TemplateView):
    template_name = "youtuber_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["youtubers"] = Youtuber.objects.all()
        return context