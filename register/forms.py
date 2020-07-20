from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class register_form (UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'fadeIn second',
        'placeholder' : 'نام کاربری',
        }),label='')
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'fadeIn second',
        'placeholder' : 'نام و نام خانوادگی',
        }),label='')
    
    nid = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'fadeIn second',
        'placeholder' : 'شماره شناسنامه',
        }),label='')
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'fadeIn second',
        'placeholder' : 'ایمیل',
        }),label='')

    password1 = forms.CharField(widget=forms.PasswordInput ,label='')
    
    password2 = forms.CharField(widget=forms.PasswordInput ,label='')
    
    class Meta:
        model = User
        fields = ['username', 'name', 'nid', 'email', 'password1', 'password2']
        