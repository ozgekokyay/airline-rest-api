# AIRLINE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework


## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.
Only authenticated users can use the API services. For authentication Rest Framework Simple JWT is used. 
In this application, we have 2 different resources, so we will use the following URLS for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api-token-auth/` | POST | CREATE | Create a new authentication token
`airline/` | POST | CREATE | Create a new airline
`airline/` | GET | READ | Get all airlines
`airline/:id` | PATCH | UPDATE | Update airline
`airline/:id` | GET | READ | Get a single airline
`airline/:id` | POST | DELETE | Delete airline
`aircraft`| POST | CREATE | Create a new aircraft
`aircraft/:id` | PATCH | UPDATE | Update an aircraft
`aircraft/:id` | GET | READ | Get a single aircraft
`aircraft/:id` | POST | DELETE | Delete aircraft

