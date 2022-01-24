from django.shortcuts import redirect, render
from menu.models import Profile
from .forms import AddContactInfo, UpdateProfile

# Create your views here.

def profile(request):
    if request.method == 'POST':
        userUpdateForm = UpdateProfile(request.POST, instance= request.user)
        addContactInfo = AddContactInfo(request.POST, instance=request.user.profile)

        if userUpdateForm.is_valid() and addContactInfo.is_valid():
            userUpdateForm.save()
            addContactInfo.save()
            return redirect('profile')

    else:
        userUpdateForm = UpdateProfile(instance= request.user)
        addContactInfo = AddContactInfo(instance=request.user.profile)
    return render(request, 'menu/profile.html', {'userUpdate': userUpdateForm, 'addContact':addContactInfo})
