from django.db import models

# Create your models here.


class sign_up (models.Model):
    
    first_Name = models.CharField(max_length=200)
    last_Name=models.CharField(max_length= 100)
    
    primaryPhone = models.IntegerField()
    secondaryPhone= models.IntegerField()
    
    email = models.EmailField (max_length=1000,primary_key=True)
    
    dob = models.DateField()
    

class orders(models.Model):
    pass 
class auth_users (models.Model):
    pass
class menuCategory(models.Model):
    menuName = models.CharField(max_length=200)
    
class menu (models.Model):
    category_Id = models.ForeignKey(menuCategory, on_delete=models.PROTECT,related_name="Category_ID",default=None)
    name = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=30)
    price = models.IntegerField(null = False)

