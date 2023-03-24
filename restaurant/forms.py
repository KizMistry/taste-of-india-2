from .models import Review, Booking, Table
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'date', 'time', 'tables', 'notes',)
        widgets = {
            'date': DateInput(),
            # 'time': TimeInput(),
        }
