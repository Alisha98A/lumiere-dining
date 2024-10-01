"""
URL configuration for the restaurant_booking_system project.

Routes requests to the admin site and the bookings app.
"""
from django.contrib import admin
from django.urls import path, include
from bookings.views import home_view
from bookings import views as index_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')), 
        # Django's built-in password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]