from rest_framework import authentication
from test_app.models import AnotherTestModel, AThirdModel, TestModel
from .serializers import (
    AnotherTestModelSerializer,
    AThirdModelSerializer,
    TestModelSerializer,
)
from rest_framework import viewsets


class TestModelViewSet(viewsets.ModelViewSet):
    serializer_class = TestModelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TestModel.objects.all()


class AnotherTestModelViewSet(viewsets.ModelViewSet):
    serializer_class = AnotherTestModelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = AnotherTestModel.objects.all()


class AThirdModelViewSet(viewsets.ModelViewSet):
    serializer_class = AThirdModelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = AThirdModel.objects.all()
