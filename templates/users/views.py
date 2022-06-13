from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import singUpForm
from .forms import UserUpdateForm,ProfieUpdateForm,profileModel
from .models import profileModel


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

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfieUpdateForm(
            request.POST, request.FILES, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfieUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)