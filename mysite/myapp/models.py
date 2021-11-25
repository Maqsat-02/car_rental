from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField('email', max_length=60, unique=True)
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)
    phone = models.CharField('phone number',max_length=20)
    address = models.CharField('address', max_length=255)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    last_login = models.DateTimeField('last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True




class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


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
    Customer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
