"""
URL configuration for the restaurant_booking_system project.

Routes requests to the admin site and the bookings app.
"""
from django.contrib import admin
from django.urls import path, include
from bookings.views import home_view
from bookings import views as index_views


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')), 
]