# import os
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from django.urls import path
# import chat.routing

# application = ProtocolTypeRouter({

#     # WebSocket chat handler
#     "websocket": AuthMiddlewareStack(
#             URLRouter(
#                 chat.routing.websocket_urlpatterns
#             )
#         )       
# })