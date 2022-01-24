from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile
from django.forms import ModelForm

class UpdateProfile(ModelForm):
    class Meta:
        model = User
        fields = ['username',]
        
class AddContactInfo(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']
