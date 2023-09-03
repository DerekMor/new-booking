from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'canceled')
    list_filter = ('canceled',)


def cancel_bookings(modeladmin, request, queryset):
    queryset.update(canceled=True)

    
cancel_bookings.short_description = "Cancel selected bookings"
