
from rest_framework import routers

from .views import PlayerViewSet

router = routers.SimpleRouter()

router.register(r'player', PlayerViewSet,
                basename="player")

urlpatterns = router.urls


player_list = PlayerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
player_detail = PlayerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})