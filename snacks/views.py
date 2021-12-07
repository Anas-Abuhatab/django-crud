from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView ,UpdateView
# Create your views here.


from .models import Snack
from django.urls import reverse_lazy


class SnackListView(ListView):
    template_name = 'snack_List.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'Snack_Detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack_Create.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']
    success_url = reverse_lazy('List_View')

class SnackUpdateView(UpdateView):
    template_name = 'SnackUpdate.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']
    success_url = reverse_lazy('List_View')

class SnackDeleteView(DeleteView):
    template_name = 'SnackDelete.html'
    model = Snack
    success_url = reverse_lazy('List_View')
