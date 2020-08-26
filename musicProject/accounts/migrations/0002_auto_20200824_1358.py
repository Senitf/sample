# Generated by Django 3.0.8 on 2020-08-24 13:58

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicuser',
            name='profile_image',
            field=models.ImageField(default='profile_images/default_image/default.jpeg', upload_to=accounts.models.MusicUser.get_file_path),
        ),
    ]