# Generated by Django 4.1.2 on 2022-10-24 14:47

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_remove_member_name_member_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='location',
        ),
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='lga',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='local Governemnt Area'),
        ),
        migrations.AddField(
            model_name='member',
            name='state_of_origin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='tribe',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]