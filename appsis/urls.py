from django.urls import path, include
from rest_framework import routers
from .views import PersonaViewSet

router = routers.DefaultRouter()
router.register('personas', PersonaViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]

