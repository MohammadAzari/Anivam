from django.urls import path

from .views import basic_chat, room

urlpatterns = [
    path('', basic_chat, name='basic_chat'),
    path('<str:room_name>/', room, name='room')
]
