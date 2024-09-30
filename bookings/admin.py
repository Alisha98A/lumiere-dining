from django.contrib import admin
from .models import Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_date', 'booking_details')
    search_fields = ('user__email', 'booking_details')

admin.site.register(Booking, BookingAdmin)
