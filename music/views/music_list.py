from django.http import HttpResponse
from django.views.generic import TemplateView

from music.models import Track, Like


def set_liked(tracks, user):
    if user.is_authenticated():
            likes = Like.objects.filter(user=user, track__in=tracks)
    else:
            likes = []
    tr_id_list = [l.track.id for l in likes]
    for tr in tracks:
        tr.liked = tr.id in tr_id_list

page_size=30
class MusicList(TemplateView):
    template_name = 'music_list.html'

    def get_context_data(self, **kwargs):
        data = super(MusicList,self).get_context_data(**kwargs)
        data['objects_list']=Track.objects.all()[:page_size]
        set_liked(data['objects_list'], self.request.user)
        data['likes_dict']=Track.objects.all()[:page_size]
        return data

class MusicListAjax(TemplateView):
    template_name = 'music_list_ajax.html'

    def get_context_data(self, **kwargs):
        page = int(self.request.GET['page']) if 'page' in self.request.GET else 0
        offset=page_size*page + 1
        offset_next=page_size*(page+1)
        data = super(MusicListAjax,self).get_context_data(**kwargs)
        data['objects_list']=Track.objects.all()[offset:offset_next]
        set_liked(data['objects_list'], self.request.user)
        return data