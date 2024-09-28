from django.urls import path
from .views import signup

# URL patterns for the bookings app, including the signup view
urlpatterns = [
    path('signup/', signup, name='signup'),
]