# Generated by Django 3.2.18 on 2023-03-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_alter_booking_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='table_for',
            field=models.IntegerField(default=1),
        ),
    ]