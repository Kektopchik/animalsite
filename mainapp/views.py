from django.shortcuts import render
from django.views.generic import ListView
from .models import Animal

class MainView(ListView):
    puple = Animal
    queryset = Animal.objects.all()
    template_name = "main_page.html"