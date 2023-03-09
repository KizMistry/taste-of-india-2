from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

GUESTS = (
    (1, "1"), (2, "2"), (3, "3"), (4, "4"),
    (5, "5"), (6, "6"), (6, "6+"))

TIMES = (
    ("11 AM", "11 AM"), ("11:30 AM", "11:30 AM"),
    ("12 PM", "12 PM"), ("12:30 PM", "12:30 PM"),
    ("1 PM", "1 PM"), ("1:30 PM", "1:30 PM"),
    ("2 PM", "2 PM"), ("2:30 PM", "2:30 PM"),
    ("3 PM", "3 PM"), ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"), ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"), ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"), ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"), ("7:30 PM", "7:30 PM"),
    ("8 PM", "8 PM"), ("8:30 PM", "8:30 PM"),
    ("9 PM", "9 PM"), ("9:30 PM", "9:30 PM"),
    ("10 PM", "10 PM"), ("10:30 PM", "10:30 PM"),)


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    guests = models.IntegerField(choices=GUESTS, default=2)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=20, choices=TIMES, default="6 PM")
    time_booked = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"


class Post(models.Model):

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


class Comment(models.Model):

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
