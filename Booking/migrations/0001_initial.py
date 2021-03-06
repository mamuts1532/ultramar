# Generated by Django 4.0 on 2021-12-18 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.PositiveIntegerField(unique=True)),
                ('loading_port', models.PositiveIntegerField()),
                ('discharge_port', models.PositiveIntegerField()),
                ('ship_arrival_date', models.DateField(blank=True)),
                ('ship_departure_date', models.DateField(blank=True)),
            ],
        ),
    ]
