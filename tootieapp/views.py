from django.shortcuts import render
from django.views.generic import ListView
from tootieapp.models import Village

class IndexView(ListView):
    template_name = "index.html"
    model = Village
    village_list = Village.objects.all()

    def get_queryset(self):
        print(self.village_list)
        return self.village_list
