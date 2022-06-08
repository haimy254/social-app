from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",home_view,name='home'),
    path('register/',registerPage, name="register"),
    path('logout/', logout, name ='logout'),
    path('login/',login,name="login"),
    path('imageform/',image_view,name="imageform"),
    path('profile/',profile,name="profile"),
    path('show_images/',display_images,name='all_images'),
    path("search/",search, name="search"),
    path('success', success, name = 'success'),
    path('delete_image/<int:image_id>',delete_image,name='delete_image'),
]




if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)