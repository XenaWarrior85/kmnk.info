from django.db import models
from django.utils import timezone


# Модели справочников, подлежащие замене на API надёжных первоисточников

class PlaceAddress(models.Model):
    line = models.CharField(max_length=200)
    number = models.IntegerField(null=False)
    dop = models.CharField(max_length=100)
    # photo = models.ImageField()

