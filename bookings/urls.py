from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import home_view, signup, custom_login, dashboard, profile

# URL patterns for the bookings app
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', views.custom_login, name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('profile/', profile, name='profile'),
]