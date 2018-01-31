from channels.routing import route,include
from apps.users.consumers import ws_message, ws_connect, ws_disconnect


notifications_routing = [
    route("websocket.connect", ws_connect, path=r"^/$"),
    route("websocket.receive", ws_message, path=r"^/$"),
    route("websocket.disconnect", ws_disconnect, path=r"^/$")
]

channel_routing = [
    include(notifications_routing, path=r"^/notifications")
]