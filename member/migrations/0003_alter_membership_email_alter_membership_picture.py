# Generated by Django 4.0.5 on 2022-12-16 04:34

from django.db import migrations, models
import member.models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_membership_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membership',
            name='picture',
            field=models.ImageField(blank=True, default='static\x07ssets\\img\\images\\personalized\x07vatar.png', null=True, upload_to=member.models.upload_image_path),
        ),
    ]
