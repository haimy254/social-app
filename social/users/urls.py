from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",home_view,name='home'),
    path("register/",register_request, name="register"),
    path('login/',login_request,name="login"),
    path(r'logout/',user_logout,name='user_logout'),
    path('imageform/',add_image,name="imageform"),
    path('profile/',profile_view,name="profile"),
    path('show_images/',display_images,name='all_images'),
    path("search/",search, name="search"),
    path('get_update/<int:image_id>',get_update,name='get_update'),
    path('profileform/',profile,name="profileform"),
    path('success', success, name = 'success'),
    path('delete_image/<int:image_id>',delete_image,name='delete_image'),
]




if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)