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
        (2, '2 seats'),
        (4, '4 seats'),
        (6, '6 seats'),]


class Table(models.Model):

    number = models.PositiveIntegerField()
    size = models.IntegerField(choices=SEATING_CHOICES, default=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'Table {self.number} ({self.size} seats)'


class Booking(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    phone = models.CharField(max_length=20, default='')
    date = models.DateField()
    # TIMES = int(
    #     (12:00, "12:00 PM"), (13:00, "1:00 PM"),
    #     (14:00, "2:00 PM"), (15:00, "3:00 PM"),
    #     (16:00, "4:00 PM"), (17:00, "5:00 PM"),
    #     (18:00, "6:00 PM"), (19:00, "7:00 PM"),
    #     (20:00, "8:00 PM"), (21:00, "9:00 PM"),
    #     (22:00, "10:00 PM"),)
    time = models.TimeField(default=time(12, 12))
    tables = models.ManyToManyField(Table)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} ({self.date} {self.time})'


# class Booking(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     guests = models.IntegerField(choices=GUESTS, default=2)
#     day = models.DateField()
#     time = models.CharField(max_length=20, choices=TIMES, default="6:00 PM")
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="bookings")

#     def __str__(self):
#         return f"{self.name} | day: {self.day} | time: {self.time}"


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
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review {self.body} by {self.name}'
