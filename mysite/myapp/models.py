from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=255)


class Vehicle(models.Model):
    model = models.CharField(max_length=250)
    year = models.CharField(max_length=10)
    mileage = models.BigIntegerField()
    number_pass = models.IntegerField()
    per_day = models.IntegerField()
    stereo = models.CharField(max_length=255)
    transmission = models.CharField(max_length=20)
    image = models.ImageField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Rental(models.Model):
    date_out = models.DateField()
    date_return = models.DateField()
    day_cost = models.IntegerField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
