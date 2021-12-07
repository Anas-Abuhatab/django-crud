from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView ,UpdateView
# Create your views here.



from .models import Snack


class SnackListView(ListView):
    template_name = ''
    model = Snack


class SnackDetailView(DetailView):
    template_name = ''
    model = Snack

class SnackCreateView(CreateView):
    template_name = ''
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = ''
    model = Snack

class SnackDeleteView(DeleteView):
    template_name = ''
    model = Snack
