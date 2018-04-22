# ACMEConferences-Django

Event registration Django Microservice for AcmeConference.

API ACCESS

To obtain a authorization token the request that must be send with curl is that: 

curl -X POST -d "username=acmeconferences&password=4cm3c0nf" http://127.0.0.1:8000/reservations/api-token-auth/

The response is:

{"token":"12cfa6232776a3213193c9a43c1c5ba27c68d5e2"}
