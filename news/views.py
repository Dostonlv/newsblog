from django.shortcuts import render
from django.views.generic import ListView
from .models import News

# Create your views here.
class HomePageView(ListView):
    template_name='home.html'
    model=News