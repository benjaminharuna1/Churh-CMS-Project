# Generated by Django 4.1.2 on 2022-12-08 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='new_believer_school',
        ),
        migrations.RemoveField(
            model_name='member',
            name='pays_tithe',
        ),
        migrations.RemoveField(
            model_name='member',
            name='schooling',
        ),
        migrations.RemoveField(
            model_name='member',
            name='working',
        ),
    ]