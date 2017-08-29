from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    direct_line = models.CharField(max_length=100, null=True, blank=True)
    other_phone = models.CharField(max_length=100, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
