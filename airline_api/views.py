from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view
from .models import Airline, Aircraft
from .serializers import AirlineSerializer, AircraftSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.user

            return Response({
                'token': str(serializer.validated_data['access']),
            })

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

class AirlineRetrieveOrUpdateOrDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #retrieve
    def get(self, request, airline_id, *args, **kwargs):
        try:
            airline_instance = Airline.objects.get(id=airline_id)
            serializer = AirlineSerializer(airline_instance)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Airline.DoesNotExist:
            return Response(
                {"res" : "Airline with id does not exists"},
                status = status.HTTP_400_BAD_REQUEST
            )

    # update
    def patch(self, request, airline_id, *args, **kwargs):
        try:
            airline_instance = Airline.objects.get(id=airline_id)
            serializer = AirlineSerializer(instance=airline_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Airline.DoesNotExist:
            return Response(
                {"res": "Airline with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

    # delete
    def post(self, request, airline_id, *arg, **kwargs):
        try:
            airline_instance = Airline.objects.get(id=airline_id)
            airline_instance.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except Airline.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AirlineCreateOrListAll(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #create
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'callsign': request.data.get('callsign'),
            'founded_year': request.data.get('founded_year'),
            'base_airport': request.data.get('base_airport'),
            'aircraft_set': []
        }
        serializer = AirlineSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #list all
    def get(self, request, *args, **kwargs):
        airline = Airline.objects
        serializer = AirlineSerializer(airline, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class AircraftCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #create
    def post(self, request, *args, **kwargs):
        data = {
            'manufacturer_serial_number': request.data.get('manufacturer_serial_number'),
            'type': request.data.get('type'),
            'model': request.data.get('model'),
            'operator_airline': request.data.get('operator_airline'),
            'number_of_engines': request.data.get('number_of_engines')
        }
        serializer = AircraftSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AircraftRetrieveOrUpdateOrDelete(APIView):
    permission_classes = [permissions.IsAuthenticated]

    #retrieve
    def get(self, request, aircraft_id, *args, **kwargs):
        try:
            aircraft_instance = Aircraft.objects.get(id=aircraft_id)
            serializer = AircraftSerializer(aircraft_instance)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except Aircraft.DoesNotExist:
            return Response(
                {"res" : "Aircraft with id does not exists"},
                status = status.HTTP_400_BAD_REQUEST
            )
    #update
    def patch(self, request, aircraft_id, *args, **kwargs):
        try:
            aircraft_instance = Aircraft.objects.get(id=aircraft_id)
            serializer = AircraftSerializer(instance = aircraft_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Aircraft.DoesNotExist:
            return Response(
                {"res": "Aircraft with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

    #delete
    def post(self, request, aircraft_id, *args, **kwargs):
        try:
            aircraft_instance = Aircraft.objects.get(id=aircraft_id)
            aircraft_instance.delete()
            return Response(
                status = status.HTTP_204_NO_CONTENT
            )
        except Aircraft.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)



