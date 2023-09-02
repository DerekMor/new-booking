from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from datetime import datetime
from django.http import JsonResponse
from .forms import BookingForm
from datetime import date
from django.contrib import messages


def create_booking(request):
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            selected_date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            time_string = f"{time}"
            datetime_obj = datetime.strptime(f"{selected_date} {time_string}", "%Y-%m-%d %H:%M")
            hour = datetime_obj.hour
            minute = datetime_obj.minute

            today = date.today()

            if datetime_obj.date() < today:
                messages.error(request, 'Selected date cannot be in the past.')
            elif Booking.objects.filter(date=datetime_obj.date(), time=f"{hour}:{minute}", canceled=False).count() < 4:
                Booking.objects.create(user=request.user, date=datetime_obj.date(), time=f"{hour}:{minute}")
                messages.success(request, 'Booking successful!')
            else:
                messages.error(request, 'Booking slot is already full.')
        else:
            messages.error(request, 'Invalid form data. Please check your inputs.')

    else:
        form = BookingForm()

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
    opening_time = 17 
    closing_time = 23 

    available_time_slots = [
        f"{hour:02d}:{minute:02d}"
        for hour in range(opening_time, closing_time)
        for minute in [0] 
    ]

    booked_time_slots = [booking.time.strftime('%H:%M') for booking in bookings]
    available_time_slots = [slot for slot in available_time_slots if slot not in booked_time_slots]
    form = BookingForm()
    
    return render(request, 'bookings/booking_list.html', {'bookings': bookings, 'available_time_slots': available_time_slots, 'form': form})

@login_required
def fully_booked_slots(request):
    fully_booked_slots = Booking.objects.filter(canceled=False).values_list('time', flat=True)
    return JsonResponse(list(fully_booked_slots), safe=False)
    

def home(request):
    return render(request, 'bookings/home.html', {'user': request.user})