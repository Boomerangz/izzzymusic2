from django.http import HttpResponse
from django.views.generic import TemplateView

from music.models import Track

page_size=50
class MusicList(TemplateView):
    template_name = 'music_list.html'

    def get_context_data(self, **kwargs):
        data = super(MusicList,self).get_context_data(**kwargs)
        data['objects_list']=Track.objects.all()[:page_size]
        return data

class MusicListAjax(TemplateView):
    template_name = 'music_list_ajax.html'

    def get_context_data(self, **kwargs):
        page = int(self.request.GET['page']) if 'page' in self.request.GET else 0
        offset=page_size*page + 1
        offset_next=page_size*(page+1)
        data = super(MusicListAjax,self).get_context_data(**kwargs)
        tracks = Track.objects.all()[offset:offset_next]
        data['objects_list']=tracks
        return data