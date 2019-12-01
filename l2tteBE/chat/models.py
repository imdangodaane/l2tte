from django.db import models
from django.utils import timezone
from api.account.models import Login

# Create your models here.


class ChatBoxMessageModel(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    message_type = models.CharField(max_length=64, default='text')
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
