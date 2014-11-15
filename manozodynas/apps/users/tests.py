# coding: utf-8

from django_webtest import WebTest
from django.core.urlresolvers import reverse

from manozodynas.apps.users.factories import UserFactory


class LoginTestCase(WebTest):
    @classmethod
    def setUpClass(cls):
        UserFactory()

    def setUp(self):
        self.form = self.app.get(reverse('login')).forms['login']

    def test_good_login(self):
        self.form['username'] = 'test'
        self.form['password'] = 'test'
        self.form.submit().follow()

    def test_bad_login(self):
        self.form['username'] = 'test'
        self.form['password'] = 'wrong'
        self.form.submit()

    def test_no_input(self):
        self.form.submit()

    def test_no_username(self):
        self.form['password'] = 'wrong'
        self.form.submit()

    def test_no_password(self):
        self.form['username'] = 'test'
        self.form.submit()
