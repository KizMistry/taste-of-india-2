from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Meal, Booking, Table
from .forms import ReviewForm, BookingForm
from django.http import HttpResponseRedirect


# Create your views here.

class Nav(View):

    def about(request):
        return render(request, 'about.html')

    def meals(request):
        return render(request, 'meal.html')


class PostList(generic.ListView):
    model = Meal
    queryset = Meal.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


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
        all_bookings = Booking.objects.all()
        bookings = Booking.objects.filter(id=self.request.user.id)
        booking_form = BookingForm()
        return render(
            request,
            'booking_list.html',
            {
                'all_bookings': all_bookings,
                'bookings': bookings,
                'booking_form': BookingForm(),
            },
        )


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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            notes = form.cleaned_data['notes']
            table_for = form.cleaned_data['table_for']
            available_tables = Table.objects.filter(
                number=table_for, available=True)
            if len(available_tables) > 0:
                table = available_tables[0]
                table.available = False
                table.save()
                form.save()
                messages.success(request, 'Booking created successfully.')
                return HttpResponseRedirect(reverse('booking_list'))
            else:
                messages.error(request, 'No table available')
                print('error')
        return render(
            request,
            'create_booking.html',
            {
                'booking_form': BookingForm()
            },
        )
