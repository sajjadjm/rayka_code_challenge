from rest_framework import routers
from core.views import DeviceViewSet

router = routers.SimpleRouter()
router.register(r'', DeviceViewSet, basename="devices")

urlpatterns = router.urls 