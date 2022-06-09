from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import PostModel
from .forms import PostModelForm

def home(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("blog-home")
    else:
        form = PostModelForm()
    context = {
        'posts' : posts,
        'form' : form
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')


