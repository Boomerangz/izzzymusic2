# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(default=b'', max_length=255, blank=True)),
                ('album', models.CharField(default=b'', max_length=255, blank=True)),
                ('title', models.CharField(default=b'', max_length=255, blank=True)),
                ('duration', models.IntegerField(default=0, max_length=255, blank=True)),
                ('link', models.CharField(default=b'', max_length=255, blank=True)),
                ('telegram_id', models.CharField(default=b'', max_length=255, blank=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='like',
            name='track',
            field=models.ForeignKey(to='music.Track'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
