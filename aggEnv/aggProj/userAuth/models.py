from django.db import models

# Create your models here.

GENDER_CHOICES = [
   ('M', 'Male'),
   ('F', 'Female')
]

class Users(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    gender = models.CharField(default='M', choices=GENDER_CHOICES, max_length = 1)
    def __str__(self):
        return self.name
