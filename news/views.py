from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Model2

# Create your views here.
class News_view(ListView):
    model = Model2
    template_name = 'Blog_list.html'
    context_object_name = 'blogs'

class New_detail(DetailView):
    model = Model2
    template_name = 'blog_detail.html'
    context_object_name = 'blog'