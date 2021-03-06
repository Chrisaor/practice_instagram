from django.conf import settings
from django.db import models


def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '%s/%s,%s' % (instance.owner.username, pid, extension)


class Photo(models.Model):
    image = models.ImageField(upload_to=user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thumbnail_image = models.ImageField()
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=64)
    profile_photo = models.ImageField(blank=True)
