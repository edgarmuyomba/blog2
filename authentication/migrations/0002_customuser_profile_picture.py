# Generated by Django 4.0.6 on 2022-07-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default=1, upload_to='profile_pictures'),
            preserve_default=False,
        ),
    ]
