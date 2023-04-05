from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, date, timedelta
from .models import Meal, Booking, Table
from .forms import ReviewForm, BookingForm
from django.http import HttpResponseRedirect


# Create your views here.

class Nav(View):

    def home(request):
        return render(request, 'index.html')

    def about(request):
        return render(request, 'about.html')

    def meals(request):
        return render(request, 'meal.html')


class MealList(View):

    def get(self, request, *args, **kwargs):
        model = Meal
        meals = Meal.objects.filter(status=1).order_by('created_on')
        paginate_by = 6
        return render(
            request,
            'meal.html',
            {
                'meals': meals,
            },
        )


class MealDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Meal.objects.filter(status=1)
        meal = get_object_or_404(queryset, slug=slug)
        reviews = meal.reviews.filter(approved=True).order_by('created_on')
        liked = False
        if meal.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            'meal_detail.html',
            {
                'meal': meal,
                'reviews': reviews,
                'reviewed': False,
                'liked': liked,
                'review_form': ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Meal.objects.filter(status=1)
        meal = get_object_or_404(queryset, slug=slug)
        reviews = meal.reviews.filter(approved=True).order_by('created_on')
        liked = False

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.meal = meal
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            'meal_detail.html',
            {
                'meal': meal,
                'reviews': reviews,
                'reviewed': True,
                'liked': liked,
                'review_form': ReviewForm()
            },
        )


class MealLike(View):

    def post(self, request, slug):
        meal = get_object_or_404(Meal, slug=slug)

        if meal.likes.filter(id=request.user.id).exists():
            meal.likes.remove(request.user)
        else:
            meal.likes.add(request.user)

        return HttpResponseRedirect(reverse('meal_detail', args=[slug]))


class BookingView(View):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(
            account=self.request.user.id).order_by('date', 'time')
        booking_form = BookingForm()
        return render(
            request,
            'booking_list.html',
            {
                'bookings': bookings,
                'booking_form': BookingForm(),
            },
        )


class BookingDelete(View):

    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        messages.info(request, 'Your booking has been cancelled')
        return HttpResponseRedirect(reverse('booking_list'))


class BookingCreate(View):

    def get(self, request, *args, **kwargs):
        booking_form = BookingForm()
        return render(
            request,
            'create_booking.html',
            {
                'booking_form': BookingForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            notes = form.cleaned_data['notes']
            table_for = form.cleaned_data['table_for']
            form_date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            today = date.today()
            day_limit = today + timedelta(days=90)
            # checks if selected date is valid
            if ((form_date < today) or (form_date > day_limit)):
                messages.error(request, '''
                Sorry, Bookings can only be made
                within the next 90 days.''')
                print('error')
                return render(
                    request,
                    'create_booking.html',
                    {
                        'booking_form': BookingForm()
                        },
                        )
            else:
                # get all bookings from selected date
                table_booked = Booking.objects.filter(
                    date=form_date, time=time, table_for=table_for)
                # if number of guests is 2 or 6
                if table_for != 4:
                    # if less than 5 bookings at this time and date,
                    # add user id, save the booking and redirect
                    if len(table_booked) < 5:
                        form = form.save(commit=False)
                        form.account = request.user.id
                        form.save()
                        messages.success(
                            request, 'Booking created successfully')
                        return HttpResponseRedirect(reverse('booking_list'))
                    # if 5 bookings at chosen time and date, error message
                    else:
                        messages.error(
                            request,
                            'Sorry, No tables are available at this time')
                        print('error')
                # if number of guests is 4
                else:
                    # if less than 10 bookings at this time and date,
                    # add user id, save the booking and redirect
                    if len(table_booked) < 10:
                        form = form.save(commit=False)
                        form.account = request.user.id
                        form.save()
                        messages.success(
                            request, 'Booking created successfully')
                        return HttpResponseRedirect(reverse('booking_list'))
                    else:
                        messages.error(
                            request,
                            'Sorry, No tables are available at this time')
                        print('error')


class BookingUpdate(View):
    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=booking_id)
        booking_form = BookingForm(instance=booking)
        return render(
            request,
            'update_booking.html',
            {
                'booking_id': booking_id,
                'booking_form': booking_form,
            },
        )

    def post(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            notes = form.cleaned_data['notes']
            table_for = form.cleaned_data['table_for']
            form_date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            today = date.today()
            day_limit = today + timedelta(days=90)
            # checks if selected date is valid
            if ((form_date < today) or (form_date > day_limit)):
                messages.error(request, '''
                Sorry, Bookings can only be made
                within the next 90 days''')
                print('error')
                return render(
                    request,
                    'update_booking.html',
                    {
                        'booking_id': booking_id,
                        'booking_form': form,
                        },
                        )
            else:
                # get all bookings from selected date
                table_booked = Booking.objects.filter(
                    date=form_date, time=time, table_for=table_for)
                # if number of guests is 2 or 6
                if table_for != 4:
                    # if less than 5 bookings at this time and date,
                    # add user id, save the booking and redirect
                    if len(table_booked) < 5:
                        form = form.save(commit=False)
                        form.account = request.user.id
                        form.save()
                        messages.success(
                            request, 'Booking updated successfully')
                        return HttpResponseRedirect(reverse('booking_list'))
                    # if 5 bookings at chosen time and date, error message
                    else:
                        messages.error(
                            request,
                            'Sorry, No tables are available at this time')
                        print('error')
                # if number of guests is 4
                else:
                    # if less than 10 bookings at this time and date,
                    # add user id, save the booking and redirect
                    if len(table_booked) < 10:
                        form = form.save(commit=False)
                        form.account = request.user.id
                        form.save()
                        messages.success(
                            request, 'Booking updated successfully')
                        return HttpResponseRedirect(reverse('booking_list'))
                    else:
                        messages.error(
                            request,
                            'Sorry, No tables are available at this time')
                        print('error')
        return render(
            request,
            'update_booking.html',
            {
                'booking_form': BookingForm()
            },
        )
