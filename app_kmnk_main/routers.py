from rest_framework import routers
from app_place.viewsets import PlaceAddressesViewSet

router = routers.DefaultRouter()
# если бы автором кода был я, я бы написал здесь, зачем этот роутер
router.register(r'Place Address', PlaceAddressesViewSet)
