from django.contrib import admin
from .models import AnotherTestModel, TestModel

admin.site.register(TestModel)
admin.site.register(AnotherTestModel)

# Register your models here.
