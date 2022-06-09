from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import singUpForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = singUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = singUpForm()

    context = {
        'form':  form,
    }
    return render(request,'users/register.html',context)

