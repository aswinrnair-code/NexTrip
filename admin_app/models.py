from django.db import models

# Create your models here.

class add_package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField()
    duration=models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name
