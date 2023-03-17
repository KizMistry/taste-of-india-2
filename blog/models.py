from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

GUESTS = (
    (2, "1-2"), (4, "3-4"), (6, "5-6"),)

TIMES = (
    ("12:00 PM", "12:00 PM"), ("12:30 PM", "12:30 PM"),
    ("1:00 PM", "1:00 PM"), ("1:30 PM", "1:30 PM"),
    ("2:00 PM", "2:00 PM"), ("2:30 PM", "2:30 PM"),
    ("3:00 PM", "3:00 PM"), ("3:30 PM", "3:30 PM"),
    ("4:00 PM", "4:00 PM"), ("4:30 PM", "4:30 PM"),
    ("5:00 PM", "5:00 PM"), ("5:30 PM", "5:30 PM"),
    ("6:00 PM", "6:00 PM"), ("6:30 PM", "6:30 PM"),
    ("7:00 PM", "7:00 PM"), ("7:30 PM", "7:30 PM"),
    ("8:00 PM", "8:00 PM"), ("8:30 PM", "8:30 PM"),
    ("9:00 PM", "9:00 PM"), ("9:30 PM", "9:30 PM"),
    ("10:00 PM", "10:00 PM"),)


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    guests = models.IntegerField(choices=GUESTS, default=2)
    day = models.DateField()
    time = models.CharField(max_length=20, choices=TIMES, default="6:00 PM")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return f"{self.name} | day: {self.day} | time: {self.time}"


class Meal(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Review(models.Model):

    post = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"
