from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import signup, dashboard, profile

# URL patterns for the bookings app
urlpatterns = [
    path('signup/', signup, name='signup'),  
    path('dashboard/', dashboard, name='dashboard'),  
    path('profile/', profile, name='profile'),
    ]