from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
    pass

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_room"
        self.room_group_name = 'test_room_group'
        async_to_sync(self.channel_layer.group.add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({"ststus":"Connected test"}))

    def send(self):
        pass