from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    OCCUPATION_CHOICES = [
        ('STUDENT', 'Student'),
        ('EMPLOYEE', 'Employee'),
        ('OTHERS', 'Others'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, default="", null=True, blank=True, max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    email_verified = models.BooleanField(default=False)
    otp=models.IntegerField(default=0,null=True,blank=True,)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
from django.conf import settings#settings.AUTH_USER_MODEL
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    head = models.CharField(max_length=50, verbose_name="Enter the Task", default="")
    desc = models.CharField(max_length=200, verbose_name="Enter the Description", default="")

    completed = models.BooleanField(default=False, verbose_name="Task Completed")

    def __str__(self):
        return str(self.head)
