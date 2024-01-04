from django.shortcuts import render
from .models import Post
from django.views import generic

class Postlist(generic.ListView):
    queryset=Post.objects.filter(status=1).order_by('-created_on')
    template_name='index.html'

class DetailView(generic.DetailView):
    model=Post
    template_name='post_detail.html'
# Create your views here.
