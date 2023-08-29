from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('list/', views.booking_list, name='booking_list'),
    path('fully_booked_slots/', views.fully_booked_slots, name='fully_booked_slots'),
]