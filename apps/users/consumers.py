import json

from channels.layers import get_channel_layer
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationsConsumer(WebsocketConsumer):

    def connect(self):
        if self.scope["user"].is_anonymous:
            # Reject the connection
            self.accept()
        else:
            # Accept the connection
             self.accept()
        print("si")

    # Connected to websocket.receive
    def receive(self, *, text_data):
        print("here AUSDASD " + text_data)
        self.send(json.dumps("ola vengo del websocket"))

    # Connected to websocket.disconnect
    def disconnect(self, close_code):
        print("bye")
