from django.conf import settings
from django.db import models


class TestModel(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    description = models.TextField()


class AnotherTestModel(models.Model):
    "Generated Model"
    test = models.ForeignKey(
        "test_app.TestModel",
        on_delete=models.PROTECT,
        related_name="anothertestmodel_test",
    )
    description = models.CharField(max_length=256,)


class AThirdModel(models.Model):
    "Generated Model"
    email = models.EmailField(max_length=254,)
    feedback = models.TextField()


# Create your models here.
