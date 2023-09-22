from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    attack = models.IntegerField()

    def __str__(self) -> str:
        return f"Name: {self.name} - Type: {self.type} - Attack: {self.attack}"
    
class Master(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    favorite_type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"Name: {self.name} - Last Name: {self.lastname} - Favorite Type: {self.favorite_type}"
    
class Gym(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    master = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"Name: {self.name} - Type: {self.type} - Master: {self.master}"