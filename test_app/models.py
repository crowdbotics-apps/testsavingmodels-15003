from django.conf import settings
from django.db import models


class TestModel(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    description = models.TextField()


# Create your models here.
