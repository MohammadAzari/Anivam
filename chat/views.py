from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import Messages

import json

def basic_chat(request):
    return render(request, 'chat/basic_chat.html', {})

@login_required 
def room(request, room_name):  
    allm = Messages.objects.all()
    all_rooms = []
    for r in allm:
        all_rooms.append(r.room)
    if not room_name in all_rooms:
        all_rooms.append(room_name)

    return render(request, 'chat/room.html', {
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'all_rooms':all_rooms,
    })