from rest_framework import routers
from .api import NPCViewSet

router = routers.DefaultRouter()
router.register('api/npcs', NPCViewSet, 'npcs')

urlpatterns = router.urls