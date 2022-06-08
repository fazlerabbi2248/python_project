from django.shortcuts import render
from django.http import  HttpResponse
from .models import PostModel

def home(request):
    posts = PostModel.objects.all()
    return render(request,'blog/home.html',{'posts': posts})

def about(request):
    return render(request,'blog/about.html')


