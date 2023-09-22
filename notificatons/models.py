from django.db import models

# Create your models here.

class NotificationMessage(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    scheduled_date = models.DateField(blank=True, null=True)
    scheduled_time = models.TimeField(blank=True, null=True)
    is_push_message = models.BooleanField(default=False, help_text='select this field only for sending push notification')

    class Meta:
        db_table = 'notification_notification'
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'
        ordering = ('scheduled_date',)

    def __str__(self):
        return f"{self.title}"