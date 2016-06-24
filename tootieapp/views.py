from django.shortcuts import render
from django.views.generic import ListView
from tootieapp.models import Category

class IndexView(ListView):
    template_name = "index.html"
    model = Category

    pass
