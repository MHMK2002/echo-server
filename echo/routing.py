from channels.routing import URLRouter
from django.urls import path

from echo.consumers import EchoConsumer

websocket_urlpatterns = URLRouter([
    path('echo', EchoConsumer.as_asgi()),
])
