# Generated by Django 4.1.2 on 2022-12-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0002_remove_member_new_believer_school_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersubgroup',
            name='subgroup',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, to='Member.subgroup'),
        ),
    ]