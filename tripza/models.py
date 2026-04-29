from django.db import models

# Create your models here.


class user_details(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

class bookingtemp(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    package=models.CharField(max_length=200)
    price=models.CharField(max_length=10000)
    travel_date=models.DateField(max_length=100)
    travelers=models.CharField(max_length=50)
    pickup=models.CharField(max_length=1000)
    spec_req=models.CharField(max_length=1000)
    user_id=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=100,default='Pending')


class payment(models.Model):
    booking = models.ForeignKey(bookingtemp, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=200)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='success')
    created_at = models.DateTimeField(auto_now_add=True)
    