# Generated by Django 5.0.3 on 2024-04-07 12:14

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(datetime.date.today)])),
                ('end_date', models.DateField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(datetime.date.today)])),
                ('bill_to', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='booking_profile', to=settings.AUTH_USER_MODEL)),
                ('booked_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_car', to='cars.cars')),
            ],
        ),
    ]
