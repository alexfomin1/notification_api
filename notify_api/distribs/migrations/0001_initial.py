# Generated by Django 4.1.1 on 2022-09-22 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distrib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distrib_id', models.CharField(max_length=255, unique=True)),
                ('distrib_begin_time', models.DateTimeField()),
                ('distrib_end_time', models.DateTimeField()),
                ('ditrib_text', models.CharField(max_length=255)),
                ('distrib_tag', models.CharField(max_length=255)),
                ('distrib_op', models.IntegerField()),
                ('message_distrib_id', models.CharField(max_length=255)),
                ('message_client_id', models.CharField(max_length=255)),
            ],
        ),
    ]
