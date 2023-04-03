from .models import Review, Booking, Table
from django import forms
from datetime import datetime, time


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        TIME_CHOICES = [
            (time(hour=x), '{:02d}:00'.format(x)) for x in range(12, 23)]
        # TIME_CHOICES = [
        #     (time(hour=12), '{:02d}:00'.format(12)),
        #     (time(hour=13), '{:02d}:00'.format(13)),
        #     (time(hour=14), '{:02d}:00'.format(14)),
        #     (time(hour=15), '{:02d}:00'.format(15)),
        #     (time(hour=16), '{:02d}:00'.format(16)),
        #     (time(hour=17), '{:02d}:00'.format(17)),
        #     (time(hour=18), '{:02d}:00'.format(18)),
        #     (time(hour=19), '{:02d}:00'.format(19)),
        #     (time(hour=20), '{:02d}:00'.format(20)),
        #     (time(hour=21), '{:02d}:00'.format(21)),
        #     (time(hour=22), '{:02d}:00'.format(22)),
        #     ]
        model = Booking
        fields = (
            'name', 'email', 'phone', 'date', 'table_for', 'time', 'notes',)
        widgets = {
            'date': DateInput(),
            'time': forms.Select(choices=TIME_CHOICES)
        }
