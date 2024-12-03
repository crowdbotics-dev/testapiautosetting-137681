from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137681ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137681", Testconnectors137681ViewSet, basename="testconnectors137681"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
