S1 SCENARIO:
You are building a multi-city food delivery API that will be consumed by both a mobile app and a web frontend. The frontend team asks why the API must be stateless.

Question:
Explain what statelessness means in the context of REST and describe how this principle affects the way your food delivery API handles user session data between requests.

Answer:
Statelessness in REST means that the server does not store information about the client's previous requests. Each request must contain all the necessary information to process it.

In a food delivery API, user session data is not stored on the server between requests. For example, the client sends an authentication token with every request. This makes the API scalable, reliable, and easy to use across both mobile and web applications.

-------------------------------------------------------------------------------------------------

S2 SCENARIO:
You are developing a restaurant management endpoint where a mobile app submits new menu items via a POST request. Your team is debating whether to use a plain Serializer or a ModelSerializer.

Question:
Justify why ModelSerializer is the better choice for this use case, and describe at least two specific field-level validations you would add to protect the data integrity of menu items.

Answer:
ModelSerializer is a better choice because it is directly connected to the Django model. It automatically creates fields, basic validations, and methods for creating and updating menu items. This reduces the amount of code we need to write.

Two field-level validations are:

Name validation: The menu item name should not be empty and should have a minimum length.
Price validation: The price must be greater than 0 and should not accept negative values.

These validations help maintain accurate and reliable menu item data.

--------------------------------------------------------------------------------------------------

S3 SCENARIO:
You are organising the URL structure for a food ordering API that exposes three resources: Restaurants, Menus, and Orders. Currently each resource has five individual APIView classes mapped to five separate URL patterns.

Question:
Explain how refactoring this to use a ModelViewSet with a DefaultRouter reduces URL management overhead, and identify which HTTP methods are automatically handled by ModelViewSet.

Answer:
Using a ModelViewSet with DefaultRouter reduces URL management because we do not need to create separate URL patterns for each CRUD operation. The router automatically generates the required URLs and connects them to the ViewSet actions.

A ModelViewSet automatically handles these HTTP methods:

GET – Retrieve/list data
POST – Create new data
PUT – Update data
PATCH – Partially update data
DELETE – Delete data

This makes the API code shorter, cleaner, and easier to maintain.

--------------------------------------------------------------------------------------------------

S4 SCENARIO:
You are designing a dish search endpoint that returns all available dishes across 500+ restaurants. A QA engineer reports that responses take over 8 seconds on a standard connection.

Question:
Identify the most likely cause of this performance issue and justify which DRF pagination class you would choose to fix it. Compare the trade-offs between PageNumberPagination and CursorPagination for this scenario.

Answer:
The most likely cause is that the API is trying to return a very large number of dishes in a single response. This increases database processing, server load, and network response time.

I would choose CursorPagination because it is more efficient for large datasets. It returns a small number of records at a time and provides stable pagination while avoiding expensive page-number calculations.

PageNumberPagination:

Easy to understand and implement.
Users can directly access a specific page.
Can become slower for very large datasets.

CursorPagination:

Faster and more efficient for large datasets.
Provides stable results when new records are added.
Users cannot directly jump to a specific page.

For 500+ restaurants and a large number of dishes, CursorPagination is the better choice for performance and scalability.

------------------------------------------------------------------------------------------------

S5 SCENARIO:
You are debugging a food delivery API where a logged-in customer can view another customer's order history simply by changing the order ID in the URL. The IsAuthenticated permission is already applied.

Question:
Identify the specific gap in the current permission setup and explain how you would implement object-level permission to ensure each customer can only access their own orders.

Answer:
The gap is that IsAuthenticated only checks whether the user is logged in. It does not check whether the requested order belongs to that user.

To fix this, I would implement an object-level permission that checks the order's customer before allowing access.

For example:

from rest_framework.permissions import BasePermission
class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user

Then apply this permission to the order API along with IsAuthenticated:

permission_classes = [IsAuthenticated, IsOrderOwner]

This ensures that a customer can access only their own orders, even if they change the order ID in the URL.

--------------------------------------------------------------------------------------------

S6 SCENARIO:
You are optimising a restaurant discovery feature that currently stores only static latitude and longitude values in the database. A product manager requests a "find restaurants near me" option that accepts a user's address string.

Question:
Describe how you would integrate the Google Maps Geocoding API into a DRF view to convert an address string into coordinates and use those coordinates to return nearby restaurant results.

Answer:
I would first accept the user's address through a GET or POST request in the DRF view. Then, I would use the Google Maps Geocoding API with the address and API key to get the latitude and longitude.

After receiving the coordinates, I would compare them with the latitude and longitude stored for each restaurant and calculate the distance. Finally, I would return the restaurants within a selected radius, such as 5 km.

The basic flow is:

User sends an address.
DRF view sends the address to Google Geocoding API.
Google API returns latitude and longitude.
The API finds restaurants near those coordinates.
DRF serializer returns the nearby restaurants as a JSON response.

This allows users to easily find restaurants near their current location or entered address.

---------------------------------------------------------------------------------------------