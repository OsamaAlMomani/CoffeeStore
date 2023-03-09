from django.db import models

# Create your models here.


class Coffee(models.Model):
    Coffee_Name = models.CharField(max_length=100, primary_key=True)
    Coffee_Price = models.FloatField()
    Coffee_Describtion = models.CharField(max_length=2000)
    Coffee_Depot = models.IntegerField()
    def __str__(self):
        return self.Coffee_Name
        
    

# class Meal(models.Model):
#     Meal_type=models.ForeignKey()

class breakfast(models.Model):
    breakfast_Name = models.CharField(max_length=100,primary_key=True)
    breakfast_Price = models.FloatField()
    breakfast_Describtion = models.CharField(max_length=2000)
    breakfast_Depot = models.IntegerField()
    def __str__(self):
        return self.breakfast_Name

class lunch(models.Model):
    lunch_Name = models.CharField(max_length=100,primary_key=True)
    lunch_Price = models.FloatField()
    lunch_Describtion = models.CharField(max_length=2000)
    lunch_Depot = models.IntegerField()
    def __str__(self):
        return self.lunch_Name

class dinner(models.Model):
    dinner_Name = models.CharField(max_length=100,primary_key=True)
    dinner_Price = models.FloatField()
    dinner_Describtion = models.CharField(max_length=2000)
    dinner_Depot = models.IntegerField()
    def __str__(self):
        return self.dinner_Name
class Dessert(models.Model):
    Dessert_Name = models.CharField(max_length=100,primary_key=True)
    Dessert_Price = models.FloatField()
    Dessert_Describtion = models.CharField(max_length=2000)
    Dessert_Depot = models.IntegerField()
    def __str__(self):
        return self.Dessert_Name

# class User(models.Model):
#     '''
#     Id
#     name
#     Email
#     Age
#     Address
#     Order // foriegnkey
#     JDate 
#     '''
#     pass
# class Order(models.Model):
#     pass

