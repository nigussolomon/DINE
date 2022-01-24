from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as mainViews

urlpatterns = [
    path('',mainViews.home, name = 'home' ),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login.html'), name='login'),
    path('signup/', mainViews.register, name='register'),
    path('dine/', include('menu.urls'))
]
