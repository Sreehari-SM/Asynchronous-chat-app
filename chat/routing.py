from django.urls import path, re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?p<room_name>\w+)/$', consumers.ChatRoomConsumer),
    re_path(r'ws/test/$', consumers.TestConsumer)
]