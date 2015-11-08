from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length = 10,primary_key = True)
    authorID = models.CharField(max_length = 10)
    title = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 30)
    publishdate = models.DateField(max_length=15)
    price = models.FloatField()    
    
    
class Author(models.Model):
    authorID = models.CharField(max_length = 10,primary_key = True)
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    country = models.CharField(max_length = 50)