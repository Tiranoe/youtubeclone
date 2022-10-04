from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('youtubers/', views.Youtuberlist.as_view(), name="youtuber_list"),
]
