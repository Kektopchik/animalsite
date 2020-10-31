from django.shortcuts import render
from django.views.generic import ListView
from .models import Animals

class MainView(ListView):
    animal = Animals
    queryset = Animals.objects.all()
    template_name = "main_page.html"

class PetUserView(ListView):
    animal = Animals
    queryset = Animals.objects.all()
    template_name = "pets1.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals'] = Animals.objects.all()
        print(context['animals'])
        return context

