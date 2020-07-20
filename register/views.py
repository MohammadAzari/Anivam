from django.shortcuts import render
from django.contrib.auth.models import User
from . import forms

def register(request):
    username = None
    password = None
    email = None
    if request.method == "POST":
        form = forms.register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.clean_password2
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        
    else:
        form = forms.register_form()

    return render(request, 'register/register.html', {"form":form})
