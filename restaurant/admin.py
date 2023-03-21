from django.contrib import admin
from .models import Meal, Review, Booking, Table


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):

    list_display = ('meal_name', 'slug', 'status', 'created_on')
    search_fields = ['meal_name', 'description']
    prepopulated_fields = {'slug': ('meal_name',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'meal', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    list_filter = ('approved', 'created_on')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', 'time')
    search_fields = ['name',]
    list_filter = ('name', 'date', 'time')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    list_display = ('number', 'size', 'available')
    search_fields = ['number', 'size', 'available',]
    list_filter = ('number', 'size', 'available')
