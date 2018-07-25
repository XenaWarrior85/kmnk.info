from django.db import models
from django.utils import timezone


# Модели справочников, подлежащие замене на API надёжных первоисточников

class PlaceAddress(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
