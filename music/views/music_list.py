from django.db.models import Q
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
        liked = 'liked' in self.request.GET
        data = super(MusicList,self).get_context_data(**kwargs)
        data['objects_list']=Track.objects.all()
        if liked:
            data['objects_list']=data['objects_list'].filter(pk__in=(l['track_id'] for l in Like.objects.filter(user=self.request.user).values('track_id')))
            data['liked']=liked
        if 'search' in self.request.GET:
            search = self.request.GET['search']
            data['objects_list']=data['objects_list'].filter(Q(artist__icontains=search)|Q(title__icontains=search))
            data['search']=search

        data['objects_list']=data['objects_list'][:page_size]
        set_liked(data['objects_list'], self.request.user)
        data['likes_dict']=Track.objects.all()[:page_size]

        return data

class MusicListAjax(TemplateView):
    template_name = 'music_list_ajax.html'

    def get_context_data(self, **kwargs):
        liked = 'liked' in self.request.GET
        page = int(self.request.GET['page']) if 'page' in self.request.GET else 0
        offset=page_size*page + 1
        offset_next=page_size*(page+1)
        data = super(MusicListAjax,self).get_context_data(**kwargs)
        data['objects_list']=Track.objects.all()
        next_str=''
        if liked:
            data['objects_list']=data['objects_list'].filter(pk__in=(l['track_id'] for l in Like.objects.filter(user=self.request.user).values('track_id')))
            next_str += 'liked&'
        if 'search' in self.request.GET:
            search = self.request.GET['search']
            data['objects_list']=data['objects_list'].filter(Q(artist__icontains=search)|Q(title__icontains=search))
            next_str += 'search=%s&'%search
        data['objects_list']=data['objects_list'][offset:offset_next]
        set_liked(data['objects_list'], self.request.user)


        return data