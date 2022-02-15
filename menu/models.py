from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(default = 'Please add your number',validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    address = models.CharField(max_length=120, default='please add your address')
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex= r'^\+?1?\d{9,15}$', message = "Phone number must be entered in the format: '+999999999' . Up to 15 digits allowed. ") 
    restaurant_name = models.CharField(default= "Enter Your Restaurant name ", max_length= 40)
    phone_number = models.CharField(default = 'please add your number', validators=[phone_regex],max_length=17, blank= False)

    def __str__(self):
        return f"{self.restarant_name}'s Restaurant"
    
class Menu(models.Model):
    restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_name= models.CharField(max_length= 120)
    food_ingridients = models.CharField(max_length = 300)
    food_price = models.CharField(max_length= 20)
    
    def __str__(self):
        return f"{self.food_name}"