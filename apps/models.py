from django.db import models
from datetime import datetime

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country_code = models.CharField(max_length=5 , default='+91')
    phone_number = models.IntegerField(default=0)
    dob=models.DateField(default=datetime(1900,1,1))
    sex = models.CharField(max_length=10)
    bio = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    pincode = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pics')
    
class FeedbackClass(models.Model):
    email = models.CharField(max_length=100)
    feedback = models.CharField(max_length=50000)