from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, time
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

GUESTS = (
    (2, "1-2"), (4, "3-4"), (6, "5-6"),)

TIMES = (
    ("12:00", "12:00 PM"), ("13:00", "1:00 PM"),
    ("14:00", "2:00 PM"), ("15:00", "3:00 PM"),
    ("16:00", "4:00 PM"), ("17:00", "5:00 PM"),
    ("18:00", "6:00 PM"), ("19:00", "7:00 PM"),
    ("20:00", "8:00 PM"), ("21:00", "9:00 PM"),
    ("22:00", "10:00 PM"),)

SEATING_CHOICES = [
        (2, '2 Guests'),
        (4, '4 Guests'),
        (6, '6 Guests'),]


class Table(models.Model):

    number = models.PositiveIntegerField()
    size = models.IntegerField(choices=SEATING_CHOICES, default=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'Table {self.number} ({self.size} seats)'


class Booking(models.Model):
    account = models.CharField(max_length=5000, default='')
    name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    phone = models.CharField(max_length=12, default='')
    date = models.DateField()
    time = models.TimeField(default=time(12, 12))
    table_for = models.IntegerField(choices=SEATING_CHOICES, default=2)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'''
        User: {self.account}
        Name: {self.name} -
        Email: {self.email} -
        Phone: {self.phone} -
        Table booked for: ({self.date} at {self.time}) -
        Table for: {self.table_for} -
        Notes: {self.notes}
        '''

    class Meta:
        ordering = ['-date', '-time']


class Meal(models.Model):

    meal_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant_posts')
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='restaurant_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.meal_name

    def number_of_likes(self):
        return self.likes.count()


class Review(models.Model):

    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField('Your Review:')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review {self.body} by {self.name}'
