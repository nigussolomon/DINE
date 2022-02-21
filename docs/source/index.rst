.. DINE documentation master file, created by
   sphinx-quickstart on Mon Feb 21 19:00:38 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to DINE's documentation!
================================

DINE is a web app that a user can simply login and browse thorugh restaurants or add their
own restaurant and add their menus to let users browse and see what they offer.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


.. toctree::

   Getting started with DINE
   Running DINE

.. note::

   This project is under active development.


Getting started with DINE
=========================

Installing needed packages
--------------------------

To use DINE, first install these packages

On Windows

.. code-block:: console

   $ pip install django
   $ pip install django-crispy-forms

On Mac and Linux

.. code-block:: console

   $ pip3 install django
   $ pip3 install django-crispy-forms


Running DINE
============

Running without a container
---------------------------

To start your local server use the following commands

On Windows

.. code-block:: console

   $ python manage.py runserver

On Mac and Linux

.. code-block:: console

   $ python3 manage.py runserver

After you have started your local server just go to your browser and use the following url http://localhost:8000


Running with a container
------------------------

To build your image

On Windows, Mac and Linux

.. code-block:: console

   $ docker build -t {your_image_name}

To run the image you just build

On Windows Mac and Linux

.. code-block:: console

   $ docker run -it -p 8000:8000 {name_of_image_you_built}

After you have run your container just go to your browser and use the following url http://localhost:8000


Views
=====

main module views
-----------------

home view

.. code-block:: console

   def home(request):
    return render(request, 'main/home.html')


register view

.. code-block:: console

   def register(request):
      if request.method == 'POST':
         form = Registration(request.POST)
         if form.is_valid():
               form.save()
               form.cleaned_data
               return redirect('login')
      else:
         form= Registration()
         formLogin=AuthenticationForm()
      return render(request, 'main/register.html',{'form':form})




menu module views
-----------------

.. code-block:: console

   def home(request):
      context = {
         'restaurants':User.objects.all()
      }
      return render (request, 'menu/homeview.html', context)


profile view

.. code-block:: console

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


add to menu view

.. code-block:: console

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


menu view

.. code-block:: console

   def menu(request):
    context = {
        'food' : Menu.objects.all(),
        'user' : User.objects.all(),
    }
    return render(request, 'menu/menu.html', context)


Urls
====

main app Urls
-------------

.. code-block:: console

   urlpatterns = [
      path('',mainViews.home, name = 'home' ),
      path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name='login'),
      path('signup/', mainViews.register, name='register'),
      path('dine/', include('menu.urls'))
   ]


menu app Urls
-------------

.. code-block:: console

   urlpatterns = [
      path('profile/', menuViews.profile, name="profile"),
      path('menuup/', menuViews.add_to_menu, name="menuup"),
      path('menu/', menuViews.menu, name="menu"),
      path('home/', menuViews.home, name="homeview"),
   ]


Models
======

.. code-block:: console

   class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
      phone_number = models.CharField(default = 'No registered Number',validators=[phone_regex], max_length=17, blank=True) # validators should be a list
      address = models.CharField(max_length=120, default='No registered address')
      
      def __str__(self):
         return f"{self.user.username}'s Profile"
      
   class Restaurant(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      phone_regex = RegexValidator(regex= r'^\+?1?\d{9,15}$', message = "Phone number must be entered in the format: '+999999999' . Up to 15 digits allowed. ") 
      restaurant_name = models.CharField(default= "", max_length= 40)
      phone_number = models.CharField(default = "", validators=[phone_regex],max_length=17, blank= False)

      def __str__(self):
         return f"{self.user.username}'s Restaurant"
      
   class Menu(models.Model):
      restaurant= models.ForeignKey(Restaurant, on_delete=models.CASCADE)
      food_name= models.CharField(max_length= 120)
      food_ingridients = models.CharField(max_length = 300)
      food_price = models.CharField(max_length= 20)
      
      def __str__(self):
         return f"{self.food_name}"


Forms
=====

main forms
----------

.. code-block:: console

   class Registration(UserCreationForm):
      class Meta:
         model=User
         fields =['username','password1','password2']

menu forms
----------

.. code-block:: console

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


