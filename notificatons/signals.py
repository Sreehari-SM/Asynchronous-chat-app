from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NotificationMessage
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=NotificationMessage)
def notification_task(sender, instance, **kwargs):
    count = NotificationMessage.objects.all().count()
    channel_layer = get_channel_layer()
    notification_data = {
        'message': 'You have a new notification!',
        'count': count,  # You can send any data you need
    }
    async_to_sync(channel_layer.group_send)(
        'notification_group',
        {
            'type': 'send.notification',
            'notification': notification_data,
        }
    )
