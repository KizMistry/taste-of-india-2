# Generated by Django 3.2.18 on 2023-03-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(choices=[('12:00 PM', '12:00 PM'), ('1:00 PM', '1:00 PM'), ('2:00 PM', '2:00 PM'), ('3:00 PM', '3:00 PM'), ('4:00 PM', '4:00 PM'), ('5:00 PM', '5:00 PM'), ('6:00 PM', '6:00 PM'), ('7:00 PM', '7:00 PM'), ('8:00 PM', '8:00 PM'), ('9:00 PM', '9:00 PM'), ('10:00 PM', '10:00 PM')]),
        ),
    ]
