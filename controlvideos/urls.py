from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'videos.views.home'),

    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #USUARIOS
    url(r'^user/login/$', 'users.views.loguet_in'),
    url(r'^private/$', 'users.views.private'),
    url(r'^user/resetpass/$', 'users.views.reset_pass'),
    url(r'^salir/$', 'users.views.loguet_out'),

    #VIDEOS
    url(r'^video/new/$', 'videos.views.new_video'),
    url(r'^video/option/$', 'videos.views.option_video'),
    url(r'^video/info/(?P<id_video>\d+)/$', 'videos.views.info_video'),
    url(r'^video/imagen/new/(?P<id_video>\d+)/$', 'videos.views.new_imagen'),
    url(r'^actor/new/(?P<id_video>\d+)/$', 'videos.views.new_actor'),
    url(r'^actor/show/(?P<id_video>\d+)/$', 'videos.views.show_actores'),
    url(r'^actor/add/(?P<id_video>\d+)/(?P<id_actor>\d+)/$', 'videos.views.add_actor'),
)
