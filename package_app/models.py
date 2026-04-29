from django.db import models

# Create your models here.


class Package(models.Model):
    image = models.ImageField(upload_to='packages/', null=True, blank=True,default=0)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    duration=models.DecimalField(max_digits=50,decimal_places=2)

    def __str__(self):
        return self.name
