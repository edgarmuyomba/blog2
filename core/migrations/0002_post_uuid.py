# Generated by Django 4.0.6 on 2022-07-08 06:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
