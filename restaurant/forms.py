from .models import Review, Booking, Table
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'date', 'time', 'tables', 'notes',)
