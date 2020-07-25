from django.shortcuts import render
from django.contrib.auth.models import User

def basic_chat(request):
    return render(request, 'chat/basic_chat.html', {})

def room(request, room_name):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'unknown user'
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': username
    })