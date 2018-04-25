
from django.urls import path, re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps.users.consumers import NotificationsConsumer
from apps.chat.consumers import ChatConsumer


app_name = 'routing'
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
            re_path(r'^ws/notifications/$', NotificationsConsumer),
        ])
    )
})