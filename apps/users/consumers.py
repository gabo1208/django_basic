import json

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session
from urllib.parse import parse_qs


@channel_session
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Parse the query string
    params = parse_qs(message.content["query_string"])
    # Set the username in the session
    message.channel_session["username"] = 123
    # Add the user to the room_name group
    Group("chat-").add(message.reply_channel)

# Connected to websocket.receive
@channel_session
def ws_message(message):
    print(message.channel_session["username"])
    Group("chat-").send({
        "text": json.dumps({
            "text": message["text"],
            "username": 123#message.channel_session["username"],
        }),
    })

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    Group("chat-").discard(message.reply_channel)