# Generated by Django 4.1.1 on 2022-09-22 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(unique=True)),
                ('client_phone', models.IntegerField()),
                ('client_op', models.IntegerField()),
                ('client_tag', models.CharField(max_length=255)),
                ('client_zone', models.CharField(max_length=50)),
            ],
        ),
    ]
