from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.register, name = "users_register"),
    path('login/',auth_view.LoginView.as_view(template_name= 'users/login.html'),name ='users-login'),


]