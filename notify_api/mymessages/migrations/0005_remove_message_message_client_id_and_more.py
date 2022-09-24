# Generated by Django 4.0.7 on 2022-09-24 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distribs', '0006_remove_distrib_operator_remove_distrib_tag_and_more'),
        ('clients', '0006_rename_client_op_client_operator_and_more'),
        ('mymessages', '0004_rename_message_status_message_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message_client_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message_distrib_id',
        ),
        migrations.AddField(
            model_name='message',
            name='cl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client'),
        ),
        migrations.AddField(
            model_name='message',
            name='distrib',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='distribs.distrib'),
        ),
    ]