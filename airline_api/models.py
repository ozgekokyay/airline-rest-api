from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=180)
    callsign = models.CharField(max_length=180)
    founded_year = models.IntegerField()
    base_airport = models.CharField(max_length=180)

    def __str__(self):
        return self.id

class Aircraft(models.Model):
    manufacturer_serial_number = models.CharField(max_length=180)
    type = models.CharField(max_length=180)
    model = models.CharField(max_length=180)
    operator_airline = models.ForeignKey(Airline, on_delete= models.CASCADE, related_name = "aircraft_set")
    number_of_engines = models.IntegerField()

    def __str__(self):
        return self.type


