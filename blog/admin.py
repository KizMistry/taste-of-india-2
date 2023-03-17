from django.contrib import admin
from .models import Meal, Review, Booking


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):

    list_display = ('meal_name', 'slug', 'status', 'created_on')
    search_fields = ['meal_name', 'description']
    prepopulated_fields = {'slug': ('meal_name',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    list_filter = ('approved', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('name', 'day', 'time')
    search_fields = ['name',]
    list_filter = ('name', 'day', 'time')
