from channels.routing import ProtocolTypeRouter, URLRouter

from core.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(
        websocket_urlpatterns,
    ),
})
