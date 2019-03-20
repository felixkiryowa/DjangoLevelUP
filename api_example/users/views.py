from django.views import generic
from .forms import CustomUserCreationForm 

# from django.shortcuts import render

# Create your views here.
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm