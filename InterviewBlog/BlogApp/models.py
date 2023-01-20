from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    program = models.CharField(max_length=100,default="")
    batch = models.IntegerField(default=0)

def __str__(self):
    return self.user.username