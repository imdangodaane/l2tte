from rest_framework import serializers
from api.account.models import Login
from .models import ChatBoxMessageModel


class ChatBoxMessageSerializer(serializers.ModelSerializer):
    class Meta:
        models = ChatBoxMessageModel
        fields = ['text', 'user']