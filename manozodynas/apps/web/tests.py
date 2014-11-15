from django.core.urlresolvers import reverse

from django_webtest import WebTest


class IndexTestCase(WebTest):
    def test_index_page(self):
        self.app.get(reverse('index'))
