from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.Patientreg, name='register'),
    path('Login/', views.Login, name='Login'),


]