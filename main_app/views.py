from unicodedata import name
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Youtuber:
    def __init__(self, name, image, language):
        self.name = name
        self.image = image
        self.language = language

youtubers = [
    Youtuber("CS Dojo", "https://yt3.ggpht.com/ytc/AMLnZu9dupLKLe6WOebxccdC3Im4aHMfCR9M4GjydKOZ=s176-c-k-c0x00ffffff-no-rj", 
        "YK Sugi, the YouTuber who runs CS Dojo, used to work as a software developer at Google. Now, he shares his expertise with over 1.6 million subscribers through step-by-step tutorials on a whiteboard and easy-to-follow demonstrations. Usually writes in python and Javascript."),
    Youtuber("Derek Banas","https://yt3.ggpht.com/ytc/AMLnZu9EUj1l1-PdMXDI0oD3UTcMypwZrnRKBy_eAZ53TA=s176-c-k-c0x00ffffff-no-rj",
        "Derek Banas begins his YouTube videos with the friendly welcome, 'Well, hello internet!' The YouTuber uploads tutorials on all sorts of topics, but his main areas of expertise include programming, web design, and mobile development. Usually writes in HTML, CSS and SQL"),
    Youtuber("freeCodeCamp","https://yt3.ggpht.com/ytc/AMLnZu9UWrGceKWaqm8AF89vuxrEt8MO3E59qOoQ785Lew=s176-c-k-c0x00ffffff-no-rj",
        "The nonprofit organization freeCodeCamp offers several comprehensive, self-paced courses on coding. Many of these courses incorporate YouTube videos with instructors who walk viewers through different modules. Usually writes in Python."),
]

class Youtuberlist(TemplateView):
    template_name = "youtuber_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["youtubers"] = youtubers
        return context