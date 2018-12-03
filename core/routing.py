from django.urls import path

from core.consumer import IMConsumer

websocket_urlpatterns = [
    path('im', IMConsumer),
]
