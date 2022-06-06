from django.urls import path
from .views import *


urlpatterns = [
    path("",home_view,name='home'),
    path('register/',registerPage, name="register"),
    path('login/',login,name="login"),
    path('logout/',logoutUser,name="logout"),
    
]