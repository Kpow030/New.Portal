
from django.urls import reverse_lazy
from  django.shortcuts import render

from .models import Post



def index(request):
    News = Post.objects.all()
    return render(request, 'index.html', context={'Post': News})



def detail(request, slug):
    new = Post.object.get(slug__iexavt=slug)
    return render(request, 'detail.html', context={'new':new})

# Create your views here.
