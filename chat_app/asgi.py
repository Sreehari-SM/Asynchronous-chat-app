import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chat import routing as app1_routing  # Import routing from app1
from notificatons import routing as app2_routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({

    # WebSocket chat handler
    "http" : django_asgi_app,
    "websocket": AuthMiddlewareStack(
            URLRouter(
                app1_routing.websocket_urlpatterns + app2_routing.websocket_urlpatterns
            )
        )       
})