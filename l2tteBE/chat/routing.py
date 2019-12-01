from django.urls import re_path, path

from . import consumers


websocket_urlpatterns = [
    # re_path(r'ws/chat/latte-chat-room$', consumers.ChatConsumer),
    path('ws/chat/<str:chat_room_type>', consumers.ChatConsumer)
]
