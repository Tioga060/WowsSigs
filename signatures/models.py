from django.db import models
from djangotoolbox.fields import DictField

class Player(models.Model):
    playerid = models.CharField(max_length = 64)
    username = models.CharField(max_length = 64)
    signature = DictField()
