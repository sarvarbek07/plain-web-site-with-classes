from django.shortcuts import render
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Blog
from django.urls import reverse_lazy

# Create your views here.

class List(ListView):
    model=Blog
    template_name='home.html'
    context_object_name='list'

class Detail(DetailView):
    model=Blog
    template_name='detail.html'
    context_object_name='i'

class Create(CreateView):
    model=Blog
    template_name='create.html'
    fields=['title','text','user']

class Update(UpdateView):
    model=Blog
    template_name='edit.html'
    fields=['title','text']

class Delete(DeleteView):
    model=Blog
    template_name='delete.html'
    success_url=reverse_lazy('home')


