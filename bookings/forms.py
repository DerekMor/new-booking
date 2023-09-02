from django import forms

class BookingForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))