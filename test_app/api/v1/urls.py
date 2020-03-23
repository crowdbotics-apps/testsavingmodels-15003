from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AnotherTestModelViewSet, AThirdModelViewSet, TestModelViewSet

router = DefaultRouter()
router.register("testmodel", TestModelViewSet)
router.register("anothertestmodel", AnotherTestModelViewSet)
router.register("athirdmodel", AThirdModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
