from django.apps import AppConfig


class NotificatonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notificatons'
    def ready(self):
        import notificatons.signals 
