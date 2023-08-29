from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Booking
from datetime import datetime

@login_required
def create_booking(request):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        datetime_obj = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

        if Booking.objects.filter(date=datetime_obj.date(), time=datetime_obj.time()).count() < 4:
            Booking.objects.create(user=request.user, date=datetime_obj.date(), time=datetime_obj.time())

    return redirect('booking_list')

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)

    if booking.user == request.user:
        booking.canceled = True
        booking.save()

    return redirect('booking_list')

