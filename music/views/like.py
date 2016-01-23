import json
import os
import uuid
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from eup import settings
from music.models import Track, Like

__author__ = 'igor'

@login_required
def like_song(request, pk):
    try:
        track = Track.objects.get(pk=pk)
        like = Like.objects.filter(user=request.user, track=track)
        if len(like)>0:
            like=like[0]
            like.delete()
            return JsonResponse({'success':True, 'liked':False})
        else:
            like = Like.objects.create(user=request.user, track=track)
            like.save()
            return JsonResponse({'success':True, 'liked':True})
    except Exception as e:
        return JsonResponse({'success':False, 'error':str(e)})

