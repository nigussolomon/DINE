from django.shortcuts import redirect, render
from menu.models import Menu, Profile, Restaurant
from django.contrib.auth.models import User
from .forms import AddContactInfo, UpdateProfile, RestaurantForm, AddtoMenu

# Create your views here.

def home(request):
    context = {
        'restaurants':User.objects.all()
    }
    return render (request, 'menu/homeview.html', context)


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
    if request.method == 'POST':
        addForm = AddtoMenu(request.POST)

        if addForm.is_valid():
            addForm.instance.restaurant = request.user.restaurant
            addForm.save()
            return redirect('menuup')
    else:
        addForm = AddtoMenu(instance = request.user.restaurant)

    context = {
        'food' : Menu.objects.all(),
        'addform':addForm
    }
    return render(request, 'menu/add_to_menu.html', context)


def menu(request):
    context = {
        'food' : Menu.objects.all(),
        'user' : User.objects.all(),
    }
    return render(request, 'menu/menu.html', context)
