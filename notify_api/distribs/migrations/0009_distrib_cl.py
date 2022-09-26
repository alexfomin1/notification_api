# Generated by Django 4.0.7 on 2022-09-26 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_alter_client_tag'),
        ('distribs', '0008_remove_distrib_cl'),
    ]

    operations = [
        migrations.AddField(
            model_name='distrib',
            name='cl',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client'),
            preserve_default=False,
        ),
    ]
