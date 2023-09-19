from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    attack = models.IntegerField()
    catch = models.DateTimeField()
    
class Master(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    favorite_type = models.CharField(max_length=20)
    
class Gym(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    master = models.CharField(max_length=20)
    pokemons = models.ManyToManyField(Pokemon)