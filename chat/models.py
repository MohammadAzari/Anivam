from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    room = models.CharField(max_length=64)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_30_messages(self):
        return Messages.objects.order_by('-time').all()[:3]