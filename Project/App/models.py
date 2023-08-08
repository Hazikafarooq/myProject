from django.db import models
from datetime import date
# Create your models here.

class Country(models.Model):
    name= models.CharField(max_length=99, default=None, unique=True)

    def __str__(self):
            return self.name

 
class City(models.Model):
    name= models.CharField(max_length=99, unique=True)
    country = models.ForeignKey(Country, on_delete= models.SET_NULL, null=True,related_name='cities')

    def __str__(self):
            return self.name

class Contact(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # email = models.EmailField(max_length=255)
    # phone = models.CharField(max_length=10, null=True)
    
    img_url = models.CharField(max_length=500, default="https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI=")
    name = models.CharField(max_length= 99, default='Hazika')
    meta_des = models.CharField(max_length= 99, default='Hello Sir, well reveal the outreach partner wala poster')
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField(default=date.today())

    def __str__(self):
            return self.name
    
class Field(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
            return self.name


class Profile(models.Model):
    img_url = models.CharField(max_length=500, default="https://media.istockphoto.com/id/1337144146/vector/default-avatar-profile-icon-vector.jpg?s=612x612&w=0&k=20&c=BIbFwuv7FxTWvh5S3vB6bkT0Qv8Vn8N5Ffseq84ClGI=")
    name = models.CharField(max_length= 99, default='Hazika')
    field = models.ForeignKey(Field, on_delete=models.SET_NULL,null=True, related_name='profiles')
    charges = models.CharField(max_length=200)
    tag = models.CharField(max_length= 99)
    rating = models.CharField(max_length=20, default=0.0)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='profiles')

    def __str__(self):
            return self.name


class Task(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.body