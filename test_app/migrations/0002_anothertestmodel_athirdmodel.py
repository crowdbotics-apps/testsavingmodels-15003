# Generated by Django 2.2.11 on 2020-03-23 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AThirdModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AnotherTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='anothertestmodel_test', to='test_app.TestModel')),
            ],
        ),
    ]
