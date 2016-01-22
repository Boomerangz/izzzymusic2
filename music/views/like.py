from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from music.models import Track, Like

__author__ = 'igor'

@login_required
def like_song(request, pk):
    try:
        track = Track.objects.get(pk=pk)
        like = Like.objects.create(user=request.user, track=track)
        like.save()
        return JsonResponse({'success':True})
    except Exception as e:
        return JsonResponse({'success':False, 'error':str(e)})

