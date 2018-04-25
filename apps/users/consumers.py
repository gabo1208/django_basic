import json

from channels.layers import get_channel_layer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        if self.scope['user'].is_anonymous:
            # Reject the connection
            await self.disconnect(-1)
        else:
            # Accept the connection
            print('USER: ' + str(self.scope['user']))
            
            await self.channel_layer.group_add(
                'notifications-' + self.scope['user'].username,
                self.channel_name
            )
            await self.accept()

    # Connected to websocket.receive
    async def receive(self, *, text_data):
        print('here AUSDASD ' + text_data)
        await self.send(
            json.dumps('ola vengo del websocket')
        )

    # Connected to websocket.disconnect
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'notifications-' + self.scope['user'].username,
            self.channel_name
        )
        print('bye')
