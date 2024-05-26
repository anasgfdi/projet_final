from django.db import models

# Create your models here.
class User(models.Model):
    name = models.fields.CharField(max_length=100)
    age = models.fields.IntegerField()
    email = models.fields.CharField(max_length=100)
    mdp = models.fields.CharField(max_length=100)