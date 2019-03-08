from rest_framework import routers
from app_place.viewsets import PlaceAddressesViewSet

router = routers.DefaultRouter()

router.register(r'Place Address', PlaceAddressesViewSet)
