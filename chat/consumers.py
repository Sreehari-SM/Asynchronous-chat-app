from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
import json

# class ChatRoomConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = f"chat{self.room_name}"
#         print("=========================")
#         await self.channel_layer.group_add(
#             self.room_name, self.room_group_name
#         )
#         await self.accept()

#         await self.channel_layer.group_send(
#             self.room_group_name,{
#                 'type' : 'tester_message',
#                 'tester' : 'tester'
#             }
#         )
    
#     async def tester_message(self, event):
#         tester = event['tester']
#         await self.send(text_data=json.dumps({
#             'tester' : tester
#         }))
    
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_name, self.room_group_name
#         )
    
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         print("=============text_data_json============", text_data_json)
#         message = text_data_json['message']
#         await self.channel_layer.group_send(
#             self.room_group_name,{
#                 'type' : 'chat_message',
#                 'message' : message
#             }
#         )
#     async def chat_message(self, event):
#         message = event['message']
#         await self.send(text_data=json.dumps({
#             'message' : message
#         }))

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_name = text_data_json['user_name']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'user_name' : user_name
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        user_name = event['user_name']
        await self.send(text_data=json.dumps({
            'message': message,
            'user_name' : user_name
        }))

    pass

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_room"
        self.room_group_name = 'test_room_group'
        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status":"Connected test"}))

    def send(self):
        pass