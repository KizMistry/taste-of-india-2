# Generated by Django 3.2.18 on 2023-03-16 16:16

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('excerpt', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_posts', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='restaurant_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='restaurant.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('guests', models.IntegerField(choices=[(2, '1-2'), (4, '3-4'), (6, '5-6')], default=2)),
                ('day', models.DateField()),
                ('time', models.CharField(choices=[('12:00 PM', '12:00 PM'), ('12:30 PM', '12:30 PM'), ('1:00 PM', '1:00 PM'), ('1:30 PM', '1:30 PM'), ('2:00 PM', '2:00 PM'), ('2:30 PM', '2:30 PM'), ('3:00 PM', '3:00 PM'), ('3:30 PM', '3:30 PM'), ('4:00 PM', '4:00 PM'), ('4:30 PM', '4:30 PM'), ('5:00 PM', '5:00 PM'), ('5:30 PM', '5:30 PM'), ('6:00 PM', '6:00 PM'), ('6:30 PM', '6:30 PM'), ('7:00 PM', '7:00 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM'), ('8:30 PM', '8:30 PM'), ('9:00 PM', '9:00 PM'), ('9:30 PM', '9:30 PM'), ('10:00 PM', '10:00 PM')], default='6:00 PM', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]