from dataclasses import field
from pyexpat import model
from django.contrib.auth.models import User
from django.forms import fields
from . models import Profile, Restaurant, Menu
from django.forms import ModelForm

class UpdateProfile(ModelForm):
    class Meta:
        model = User
        fields = ['username',]
        
class AddContactInfo(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'phone_number']

class AddtoMenu(ModelForm):
    class Meta:
        model = Menu
        fields = ['food_name', 'food_ingridients', 'food_price']
