from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

# Create your models here.

class CustomUser(AbstractUser):
    #Additional fields in here
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.email
