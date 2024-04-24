from django.db import models

# Create your models here.

class Car(models.Model):
    carname=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)
    discription=models.TextField()
    image = models.ImageField(upload_to='images/')
