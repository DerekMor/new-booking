from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from datetime import datetime
from django.http import JsonResponse

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

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(canceled=False)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def fully_booked_slots(request):
    fully_booked_slots = Booking.objects.filter(canceled=False).values_list('time', flat=True)
    return JsonResponse(list(fully_booked_slots), safe=False)
    

def home(request):
    return render(request, 'bookings/home.html', {'user': request.user})