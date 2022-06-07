from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",home_view,name='home'),
    path('register/',registerPage, name="register"),
    path('login/',login_user,name="login"),
    path('logout/',logoutUser,name="logout"),
    # path('profile/',profile_view,name="profile"),
    path('show_images/',display_images,name='all_images'),
    path("search/",search, name="search"),
    path('success', success, name = 'success'),
]




if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)