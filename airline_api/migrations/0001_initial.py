# Generated by Django 5.0 on 2023-12-16 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('callsign', models.CharField(max_length=180)),
                ('founded_year', models.IntegerField()),
                ('base_airport', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_serial_number', models.CharField(max_length=180)),
                ('type', models.CharField(max_length=180)),
                ('model', models.CharField(max_length=180)),
                ('number_of_engines', models.IntegerField()),
                ('operator_airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline_api.airline')),
            ],
        ),
    ]