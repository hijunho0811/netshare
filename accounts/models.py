from django.db import models
from django.conf import settings
import re

def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('별명',max_length=30, unique=True)
    
    picture = ProcessedImageField(
                        upload_to=user_path,
                        processors=[ResizeToFill(150,150)],
                        format='JPEG',
                        options={'quality':90},
                        blank=True,
    )
    about = models.CharField(max_length=300, blank=True)
    
