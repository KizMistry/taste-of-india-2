from .models import Review, Booking
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'guests', 'day', 'time', 'user')
