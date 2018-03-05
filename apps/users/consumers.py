import json

from channels.layers import get_channel_layer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationsConsumer(WebsocketConsumer):

    def connect(self):
        if self.scope["user"].is_anonymous:
            # Reject the connection
            self.disconnect(-1)
        else:
            # Accept the connection
            print("USER: " + str(self.scope["user"]))
            self.accept()
            async_to_sync(self.channel_layer.group_add)("notifications-" + self.scope["user"].username, self.channel_name)

    # Connected to websocket.receive
    def receive(self, *, text_data):
        print("here AUSDASD " + text_data)
        self.send(json.dumps("ola vengo del websocket"))

    # Connected to websocket.disconnect
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("notifications-" + self.scope["user"].username, self.channel_name)
        print("bye")
