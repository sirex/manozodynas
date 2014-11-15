from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'', include('manozodynas.apps.web.urls')),
    url(r'', include('manozodynas.apps.users.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    },
))
