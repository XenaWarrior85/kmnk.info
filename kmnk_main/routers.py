from rest_framework import routers
from place.viewsets import PlaceAddressesViewSet

router = routers.DefaultRouter()

router.register(r'Place Address', PlaceAddressesViewSet)
