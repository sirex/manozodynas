from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns(
    'manozodynas.apps.users.views',
    url(r'^login/$', 'login_view', name='login'),
)
