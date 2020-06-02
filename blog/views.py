from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post

#class HomePageView(TemplateView):
#   template_name = 'homepage.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class HomePageView(ListView):
    model = Post
    template_name = 'homepage.html'