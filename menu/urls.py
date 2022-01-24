from django.urls import path
from . import views as menuViews

urlpatterns = [
    path('profile/', menuViews.profile, name="profile")
]
