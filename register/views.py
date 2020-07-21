from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . import forms

def register(request):
    username = None
    email = None
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=pass1)
        user.save()
        
    # else:
    #     form = forms.register_form()

    return render(request, 'register/register.html')


def login(request):
    username = None
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(username=username, password=pass1)
        
    # else:
    #     form = forms.register_form()

    return render(request, 'register/register.html')
