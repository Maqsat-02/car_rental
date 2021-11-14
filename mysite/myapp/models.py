from django.db import models


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


class Agency(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=255)


class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=250)
    year = models.CharField(max_length=10)
    mileage = models.BigIntegerField()
    image = models.FilePathField(path="myapp/static/myapp/assets/img")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)


class Rental(models.Model):
    date_out = models.DateField()
    date_return = models.DateField()
    day_cost = models.IntegerField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


