import factory

from manozodynas.common.testutils import past
from manozodynas.apps.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = 'test'
    is_active =  True
    email_approved =  False
    is_superuser =  True
    is_staff =  True
    last_login =  factory.LazyAttribute(past(days=7))
    password = factory.PostGenerationMethodCall('set_password', 'test')
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)
    date_joined = factory.LazyAttribute(past(hours=1))

    class Meta:
        model = User
        django_get_or_create = ('username',)
