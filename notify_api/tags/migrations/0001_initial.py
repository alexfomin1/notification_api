# Generated by Django 4.0.7 on 2022-09-26 19:25

from django.db import migrations, models
import django_prometheus.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            bases=(django_prometheus.models.ExportModelOperationsMixin('tag'), models.Model),
        ),
    ]
