from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from music.views.like import like_song

from music.views.music_list import MusicList, MusicListAjax

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url('^music/ajax/', MusicListAjax.as_view()),
    url(r'^music/like/(?P<pk>\d+)$', like_song),
    url('^', MusicList.as_view()),
)