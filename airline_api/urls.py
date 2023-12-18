from django.urls import path, include

from .views import (
    AirlineCreateOrListAll,
    AirlineRetrieveOrUpdateOrDelete,
    AircraftCreate,
    AircraftRetrieveOrUpdateOrDelete,
    CustomTokenObtainPairView,

)

urlpatterns = [
    path('airline/', AirlineCreateOrListAll.as_view()),
    path('airline/<int:airline_id>', AirlineRetrieveOrUpdateOrDelete.as_view()),
    path('aircraft/', AircraftCreate.as_view()),
    path('aircraft/<int:aircraft_id>', AircraftRetrieveOrUpdateOrDelete.as_view()),
    path('api-token-auth/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

]