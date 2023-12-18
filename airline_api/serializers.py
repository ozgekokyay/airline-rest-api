from rest_framework import serializers
from .models import Airline, Aircraft
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ["id", "manufacturer_serial_number", "type", "model", "operator_airline", "number_of_engines"]


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        aircraft_set = AircraftSerializer(many=True, required=False, allow_empty=True, default=None)
        fields = ["id", "name", "callsign", "founded_year", "base_airport", "aircraft_set"]

