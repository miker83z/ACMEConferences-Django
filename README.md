# ACMEConferences-Django

Event registration Django Microservice for AcmeConference.

# Api Access

The account authorized is:

Username | Password | Token
------------ | ------------- | -------------
acmeconferences | 4cm3c0nf | 12cfa6232776a3213193c9a43c1c5ba27c68d5e2
 

## Curl (Testing) ##

To obtain an **authorization token** the request that must be send with **Curl** is that: 

*curl -X POST -d "username=acmeconferences&password=4cm3c0nf" http://127.0.0.1:8000/reservations/api-token-auth/*

The response is:

*{"token":"12cfa6232776a3213193c9a43c1c5ba27c68d5e2"}*

To obtain the event list with a **GET request** the **Curl** command is:

*curl -H "Content-Type: application/json" -H "Authorization: Token 12cfa6232776a3213193c9a43c1c5ba27c68d5e2" http://localhost:8000/events/*

**Delete Request**

*curl -X DELETE -H "Authorization: Token 12cfa6232776a3213193c9a43c1c5ba27c68d5e2" http://127.0.0.1:8000/events/id/*

## Java ##

For all request with Java ApacheHTTP the header with token authentication must be set as follow:

*httpRequest.addHeader("Authorization", "Token 12cfa6232776a3213193c9a43c1c5ba27c68d5e2");*

# Api resources

Resource | Link | Request
------------ | ------------- | -------------
Event Reservations | localhost/event_reservations/ | GET, POST
Users | localhost/users/ | GET, POST
Events | localhost/events/ | GET, POST
Single Event | localhost/events/id/ | GET, PUT, PATCH, DELETE
Single User | localhost/users/id/ | GET, PUT, PATCH, DELETE
User reservations by event | localhost/events/id/user_reservations/ | GET, POST
Single user reservation by event | localhost/events/id/user_reservations/id/ | GET, PUT, PATCH, DELETE
