from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

USER_CHOICES = [
    ('Blogger', 'Blogger'),
    ('Reader', 'Reader'),
]

class CustomUser(AbstractUser):
    location = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.date.today)
    role = models.CharField(max_length=50, choices=USER_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures')


