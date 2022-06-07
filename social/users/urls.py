from django.urls import path
from .views import *


urlpatterns = [
    path("",home_view,name='home'),
    path('register/',registerPage, name="register"),
    path('login/',login_user,name="login"),
    path('logout/',logoutUser,name="logout"),
     path('profile/',profile,name="profile"),
]