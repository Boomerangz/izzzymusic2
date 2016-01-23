import uuid
from django.contrib.auth.models import User
from django.db import models


class TelegramLink(models.Model):
    user=models.ForeignKey(User)
    chat_id=models.CharField(max_length=20)
    unique_code=models.CharField(max_length=100, default=uuid.uuid1)