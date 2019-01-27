from django.db import models
from django.utils import timezone


# Модели справочников, подлежащие замене на API надёжных первоисточников

class PlaceAddress(models.Model):
    line = models.CharField(max_length=200)
    number = models.IntegerField(null=False)
    dop = models.CharField(max_length=100)
    # photo = models.ImageField()

    class Meta:
        verbose_name = 'Адрес места'
        verbose_name_plural = 'Адреса мест'

    def __str__(self):
        return '{} {} {}'.format(self.line, self.number, self.dop)
