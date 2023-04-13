from django.db import models
from accounts.models import *

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'chat_chat_rooms'
        verbose_name = 'Chatroom'
        verbose_name_plural = 'Chatrooms'
        ordering = ('name',)

class Message(models.Model):
    text = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    user = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    room = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)

    class Meta:
        db_table = 'chat_message'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('date_added',)
