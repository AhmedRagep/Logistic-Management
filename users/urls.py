from django.urls import path
from . import views

urlpatterns = [
    path('register_sender/',views.register_sender, name='register_sender'),
    path('register_rider/',views.register_rider, name='register_rider'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout')
]
