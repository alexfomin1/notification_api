# Generated by Django 4.1.1 on 2022-09-22 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_client_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_op',
            field=models.CharField(max_length=30),
        ),
    ]
