import json
import os
import uuid
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from eup import settings
from music.models import Track, Like

__author__ = 'igor'

def temp_file_name():
    path = '/tmp/%s.mp3' % uuid.uuid1()
    return path


@login_required
def like_song(request, pk):
    try:
        track = Track.objects.get(pk=pk)
        like = Like.objects.create(user=request.user, track=track)
        like.save()
        chat_id = 1398413
        if track.telegram_id is None or track.telegram_id == "":
            import urllib
            testfile = urllib.URLopener()
            path = temp_file_name()
            testfile.retrieve(track.link, path)
            filename=path
            r = requests.post('https://api.telegram.org/bot%s/sendAudio'%settings.BOT_TOKEN, files={'audio': open(filename, 'rb')}, data={"duration":300,"chat_id":chat_id, 'performer':track.artist, 'title':track.title})
            print r.content
            r_js = json.loads(r.content)
            f_id = r_js["result"]["audio"]["file_id"]
            track.telegram_id = f_id
            track.save()
            os.remove(filename)
        else:
            r = requests.post('https://api.telegram.org/bot%s/sendAudio'%settings.BOT_TOKEN, data={"duration":track.duration,"chat_id":chat_id, 'performer':track.artist, 'title':track.title, 'audio':track.telegram_id})
            print r.content
        return JsonResponse({'success':True})
    except Exception as e:
        return JsonResponse({'success':False, 'error':str(e)})

