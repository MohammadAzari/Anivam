import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Messages
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        msgs = Messages.objects.order_by('-time').filter(room=data['room'])[:30]
        
        content = {
            'messages':self.messages_to_json(msgs),
            'command':'fetch_messages',
        }
        self.send_message(content)

    def new_messages(self, data):
        author = User.objects.get(username=data['from'])
        message = Messages.objects.create(
            author=author,
            content=data['message'],
            room=data['room'],
        )
        content = {
            'command':'new_messages',
            'message':self.message_to_json(message)
        }
        return self.send_chat_messages(content)

    def messages_to_json(self, messages):
        res = []
        for msg in messages:
            res.append(self.message_to_json(msg))
        return res

    def message_to_json(self, msg):
        return {
                'author':msg.author.username,
                'content':msg.content,
                'time':str(msg.time),
                'room':msg.room,
        }
        
    commands = {
        'fetch_messages':fetch_messages,
        "new_messages":new_messages,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
        
    def send_chat_messages(self, msg):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': msg,
                'username': self.scope["user"].username
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))