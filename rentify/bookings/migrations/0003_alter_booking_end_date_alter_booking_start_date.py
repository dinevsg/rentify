# Generated by Django 5.0.3 on 2024-04-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_booking_end_date_booking_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]