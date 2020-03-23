from rest_framework import serializers
from test_app.models import TestModel


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = "__all__"
