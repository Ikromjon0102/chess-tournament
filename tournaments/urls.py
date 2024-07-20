from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, TournamentViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'tournaments', TournamentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


