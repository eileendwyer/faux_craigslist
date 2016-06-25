from django.shortcuts import render
from django.views.generic import ListView, CreateView
from tootieapp.models import Village, Profile

class IndexView(ListView):
    template_name = "index.html"
    model = Village


class ProfileView(CreateView):
    model = Profile
    template_name = "accounts/profile_view.html"
    pass
