# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_telegramlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramlink',
            name='unique_code',
            field=models.CharField(default=uuid.uuid1, max_length=100),
        ),
    ]
