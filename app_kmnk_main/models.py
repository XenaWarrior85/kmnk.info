from django.db import models
from person.models import Person
from app_place.models import PlaceAddress
from .choices import KLASS_CHOICES


class Position(models.Model):
    name = models.CharField('Название позиции', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'


class Function(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, related_name='function')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, related_name='function')
    place = models.ForeignKey(PlaceAddress, on_delete=models.CASCADE, null=True, related_name='function')

    class Meta:
        verbose_name = 'Функция'
        verbose_name_plural = 'Функции'


class CourseName(models.Model):
    name = models.CharField('Название курса', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название курса'
        verbose_name_plural = 'Названия курсов'


class Course(models.Model):
    name = models.ForeignKey(CourseName, on_delete=models.CASCADE, null=True, related_name='course')
    klass = models.CharField(max_length=2, choices=KLASS_CHOICES)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
