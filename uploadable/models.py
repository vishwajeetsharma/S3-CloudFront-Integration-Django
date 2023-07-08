from django.db import models
from django.dispatch import receiver
import os

# Create your models here.
class datas(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", max_length=255)
    
    def __str__(self):
        return self.name
    