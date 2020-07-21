from django.shortcuts import render

def basic_chat(request):
    return render(request, 'chat/basic_chat.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })