"""
Этот файл предназначен для обработки и правильного представления данных
полученных при помощи сериализатора. Он написан в стиле CBV, основные
методы, которые обрабатывают данные прописаны в базовом классе. Их можно
переопределить путём записи в данном файле.
 Для более подробного понимания работы классов, предлагаю обратиться к
коду исходников. На Pycharm - выделите класс и нажмите Ctrl+N.
"""
from rest_framework import viewsets

from .models import PlaceAddress
from .serializers import PlaceAdressSerializer


class PlaceAddressesViewSet(viewsets.ModelViewSet):
    """
    Данный класс запрашивает данные у сериализатора, получает их и
    подготавливает для вывода в JSON.
    """
    queryset = PlaceAddress.objects.all()
    serializer_class = PlaceAdressSerializer
