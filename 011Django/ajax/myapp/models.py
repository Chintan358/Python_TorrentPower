from django.db import models

# Create your models here.
class Studnet(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  age = models.IntegerField()


  
