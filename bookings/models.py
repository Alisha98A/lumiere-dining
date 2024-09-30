from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_details = models.TextField()

    def __str__(self):
        return f"Booking by {self.user.email} on {self.booking_date}"
