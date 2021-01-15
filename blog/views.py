from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Post

def home(request):
    return render(request, 'blog/home.html', {'title':'Blog Site'})

def blog(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/blog.html',context)


def about(request):
    return render(request,'blog/about.html')