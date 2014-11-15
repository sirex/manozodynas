from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    'manozodynas.apps.web.views',
    url(r'^$', 'index_view', name='index'),
)
