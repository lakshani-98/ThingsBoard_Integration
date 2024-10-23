# ThinsBoard Sensor Dashboard API
This is a Flask application that provides secure access to ThingsBoard sensor dashboards using JWT-based authentication. The API allows users to generate access tokens and retrieve dashboard links for sensors based on predefined customer-to-sensor mappings.

**Features**

JWT Authentication:
Users must authenticate using their customer_id to receive a JWT token for accessing protected routes.

Sensor Dashboard Access:
Users can retrieve the ThingsBoard dashboard link for a specific sensor, if they have permission to aceess the details of that sensor.

Authorization Checks:
Only customers authorized for a particular sensor will be allowed to retrieve its dashboard link.

**Endpoints**

**1. Generate JWT Token**
POST /token

Generates a JWT token if the provided customer ID is valid.

Request Body:

json
Copy code
{
    "customer_id": "customer1"
}

Response:

json
Copy code
{
    "access_token": "your_jwt_token_here"
}

Status Codes:

200: Token generated successfully.
401: Invalid customer ID.

**2. Get Sensor Dashboard Link**
GET /dashboard/<sensor_id>

Retrieves the ThingsBoard dashboard link for the given sensor ID. Requires a valid JWT token.

Headers:

Authorization: Bearer <your_jwt_token_here>

Response:

{
    "link": "sensor_1_link"
}

Status Codes:

200: Dashboard link retrieved successfully.
403: Unauthorized access to the sensor.
404: Dashboard link not found.


