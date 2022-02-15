from django.urls import path
from . import views as menuViews

urlpatterns = [
    path('profile/', menuViews.profile, name="profile"),
    path('menuup/', menuViews.add_to_menu, name="menuup")
]
