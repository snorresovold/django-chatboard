from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)