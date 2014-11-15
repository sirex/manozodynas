import datetime

from django.utils import timezone


def past(**kwargs):
    def func(obj):
        return timezone.now() - datetime.timedelta(**kwargs)
    return func
