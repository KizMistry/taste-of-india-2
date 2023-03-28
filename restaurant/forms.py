from .models import Review, Booking, Table
from django import forms
from datetime import datetime, time


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class DateInput(forms.DateInput):
    input_type = 'date'


# class TimeInput(forms.TimeInput):
#     input_type = 'time'


class BookingForm(forms.ModelForm):
    class Meta:
        TIME_CHOICES = [
            (time(hour=x), '{:02d}:00'.format(x)) for x in range(12, 23)]
        model = Booking
        fields = (
            'name', 'email', 'phone', 'date', 'table_for', 'time', 'notes',)
        widgets = {
            'date': DateInput(),
            'time': forms.Select(choices=TIME_CHOICES)
        }
