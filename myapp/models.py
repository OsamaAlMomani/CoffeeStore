from django.db import models

# Create your models here.
class menu (models.Model):
    name = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=30)
    price = models.IntegerField()

class sign_up (models.Model):
    first_Name = models.CharField(max_length=200)
    last_Name=models.CharField(max_length= 100)
    email = models.EmailField (max_length=1000,primary_key=True)
    dob = models.DateField()
    
class sign_in(models.Model):
    pass

class orders(models.Model):
    pass 
class auth_users (models.Model):
    pass
