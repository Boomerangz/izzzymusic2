import json
import os
import uuid
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from eup import settings
from music.models import Track, Like, TelegramLink


def temp_file_name():
    path = '/tmp/%s.mp3' % uuid.uuid1()
    return path


# {"update_id":202480832,
# "message":{"message_id":8,"from":{"id":1398413,"first_name":"Igor","last_name":"Zygin"},"chat":{"id":1398413,"first_name":"Igor","last_name":"Zygin","type":"private"},"date":1450995712,"text":"asd"}}
def set_id(chat_id, uu_code):
    print uu_code
    telegram_link = TelegramLink.objects.filter(unique_code=uu_code[0])
    if len(telegram_link)>0:
	print telegram_link
        telegram_link=telegram_link[0]
        telegram_link.chat_id=chat_id
        telegram_link.save()


def income_message(request):
        if request.method=='POST':
            print "POST"
            print request.body
            text = unicode(request.body)#.encode('utf8')
            print text
            body = json.loads(text)
            print body
            chat_id = body["message"]["chat"]["id"]
            response = {}
            try:
                text = body["message"]["text"].encode('utf8')
                print text
                text_list = text.split(" ")
                print text_list
                if text_list[0][0]=="/":
                    if text_list[0]=="/id":
                        set_id(chat_id, text_list[1:])
            except Exception as e:
                print e
                pass
            return JsonResponse(response)
        else:
            print "ELSE"
        return JsonResponse({'method': 'sendMessage', 'text':'GOT IT'})

@login_required
def send_song(request, pk):
    telegram_link = TelegramLink.objects.filter(user=request.user)
    if len(telegram_link)>0 and len(telegram_link[0].chat_id)>0:
        try:
            track = Track.objects.get(pk=pk)
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
    else:
        if len(telegram_link)==0:
            telegram_link = TelegramLink.objects.create(user=request.user)
        else:
            telegram_link = telegram_link[0]
        return JsonResponse({'success':False, 'telegram':False, "code":str(telegram_link.unique_code)})
