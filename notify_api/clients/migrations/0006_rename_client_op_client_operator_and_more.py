# Generated by Django 4.0.7 on 2022-09-24 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_remove_client_client_id_alter_client_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_op',
            new_name='operator',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_tag',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='client_zone',
            new_name='zone',
        ),
    ]
