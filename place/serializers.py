"""
Это файл нужен для преобразования сложных данных, таких как наборы
запросов и экземпляры моделей в собственные типы данных Python,
которые затем можно легко преобразовывать в JSON, XML и т.п.

"""

from rest_framework import serializers

from .models import PlaceAddress

__author__ = 'Sergey Ivanov'
__company__ = 'IvanovsCo'


class PlaceAdressSerializer(serializers.ModelSerializer):
    """
    Данный класс позволяет серелизовать данные модели указанные в class
    Meta и подготовить их для вывода в JSON вид.
    """
    class Meta:
        model = PlaceAddress
        fields = '__all__'
