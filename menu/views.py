from django.shortcuts import redirect, render
from menu.models import Profile
from .forms import AddContactInfo, UpdateProfile, RestaurantForm

# Create your views here.

def profile(request):
    if request.method == 'POST':
        userUpdateForm = UpdateProfile(request.POST, instance= request.user)
        addContactInfo = AddContactInfo(request.POST, instance=request.user.profile)
        restaurantForm = RestaurantForm(request.POST, instance=request.user.restaurant)


        if userUpdateForm.is_valid() and addContactInfo.is_valid():
            userUpdateForm.save()
            addContactInfo.save()
            return redirect('profile')
        
        if restaurantForm.is_valid():
            restaurantForm.save()
            return redirect('profile')

    else:
        userUpdateForm = UpdateProfile(instance= request.user)
        addContactInfo = AddContactInfo(instance=request.user.profile)
        restaurantForm = RestaurantForm(instance = request.user.restaurant)
    return render(request, 'menu/profile.html', {'userUpdate': userUpdateForm, 'addContact':addContactInfo, 'restaurant': restaurantForm} )

def add_to_menu(request):
    return render(request, 'menu/add_to_menu.html')
