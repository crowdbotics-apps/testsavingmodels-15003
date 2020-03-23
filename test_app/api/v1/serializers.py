from rest_framework import serializers
from test_app.models import AnotherTestModel, AThirdModel, TestModel


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = "__all__"


class AnotherTestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnotherTestModel
        fields = "__all__"


class AThirdModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AThirdModel
        fields = "__all__"
