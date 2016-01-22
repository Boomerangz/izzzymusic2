from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from music.views.music_list import MusicList, MusicListAjax

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url('^music/ajax/', MusicListAjax.as_view()),
    url('^', MusicList.as_view()),
)
