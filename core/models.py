from django.db import models
from authentication.models import CustomUser
import uuid

class Post(models.Model):
    caption = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures')
    date_added = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.caption