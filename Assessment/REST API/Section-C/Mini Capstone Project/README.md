# Food Delivery REST API Backend

A fully functional, clean, and beginner-friendly Django REST Framework (DRF) backend API for a Food Delivery application. Built using DRF best practices including `ModelViewSet`, `DefaultRouter`, `PageNumberPagination`, `TokenAuthentication`, field-level validation, and custom query filtering.

---

## Table of Contents

- [Technologies Used](#technologies-used)
- [Project Architecture & Structure](#project-architecture--structure)
- [Installation & Setup Guide](#installation--setup-guide)
  - [1. Virtual Environment Setup](#1-virtual-environment-setup)
  - [2. Package Installation](#2-package-installation)
  - [3. Database Migrations](#3-database-migrations)
  - [4. Superuser Creation](#4-superuser-creation)
  - [5. Running the Development Server](#5-running-the-development-server)
- [Authentication Guide](#authentication-guide)
- [API Endpoints Reference](#api-endpoints-reference)
- [Sample Requests & Responses](#sample-requests--responses)
  - [1. Obtaining an Auth Token](#1-obtaining-an-auth-token)
  - [2. Category Resource](#2-category-resource)
  - [3. MenuItem Resource](#3-menuitem-resource)
  - [4. Order Resource](#4-order-resource)
- [Validation Rules & Examples](#validation-rules--examples)
- [Pagination Example](#pagination-example)
- [Status Filtering Example](#status-filtering-example)
- [Sample Test Data](#sample-test-data)
- [Running Unit Tests](#running-unit-tests)
- [Postman Testing Screenshots](#postman-testing-screenshots)

---

## Technologies Used

- **Python**: 3.11+
- **Django**: 4.2+
- **Django REST Framework**: 3.14+
- **Database**: SQLite3 (default)
- **Authentication**: Token Authentication (`rest_framework.authtoken`)

---

## Project Architecture & Structure

```
food_delivery/
│
├── manage.py                   # Django management script
│
├── food_delivery/              # Project configuration module
│   ├── __init__.py
│   ├── settings.py             # App settings, REST_FRAMEWORK config, INSTALLED_APPS
│   ├── urls.py                 # Root URL router inclusion
│   ├── asgi.py
│   └── wsgi.py
│
└── api/                        # REST API app module
    ├── __init__.py
    ├── admin.py                # Model registration for Django Admin
    ├── apps.py                 # App configuration
    ├── models.py               # Category, MenuItem, Order models
    ├── serializers.py          # ModelSerializers with field-level validations
    ├── views.py                # CategoryViewSet, MenuItemViewSet, OrderViewSet
    ├── urls.py                 # DRF DefaultRouter and token endpoint setup
    ├── tests.py                # Automated API tests (10 test cases)
    └── migrations/             # Database migration files
```

---

## Installation & Setup Guide

### 1. Virtual Environment Setup

Navigate to the project root directory and create a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Package Installation

Install Django and Django REST Framework:

```bash
pip install django djangorestframework
```

### 3. Database Migrations

Apply database migrations to set up core Django tables, token authentication tables, and application models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Superuser Creation

Create an admin user to access the Django Admin panel at `/admin/`:

```bash
python manage.py createsuperuser
```

### 5. Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## Authentication Guide

The Order API endpoints are protected and require `TokenAuthentication`.

### 1. Obtain Auth Token
Send a `POST` request to `/api/token/` with user credentials:

- **Endpoint**: `POST /api/token/`
- **Request Body**:
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
      "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
  }
  ```

### 2. Passing the Token in Requests
For protected endpoints (`/api/orders/`), include the token in the `Authorization` HTTP header:

```http
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

---

## API Endpoints Reference

### Token Endpoint

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/token/` | Obtain auth token for user | No |

### Category Endpoints (`ModelViewSet`)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/categories/` | List all food categories | No |
| `POST` | `/api/categories/` | Create a new category | No |
| `GET` | `/api/categories/<id>/` | Retrieve details of a specific category | No |
| `PUT` | `/api/categories/<id>/` | Update all fields of a category | No |
| `PATCH` | `/api/categories/<id>/` | Partially update a category | No |
| `DELETE` | `/api/categories/<id>/` | Delete a category | No |

### MenuItem Endpoints (`ModelViewSet`)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/menu-items/` | List all menu items | No |
| `POST` | `/api/menu-items/` | Create a new menu item | No |
| `GET` | `/api/menu-items/<id>/` | Retrieve details of a specific menu item | No |
| `PUT` | `/api/menu-items/<id>/` | Update all fields of a menu item | No |
| `PATCH` | `/api/menu-items/<id>/` | Partially update a menu item | No |
| `DELETE` | `/api/menu-items/<id>/` | Delete a menu item | No |

### Order Endpoints (`ModelViewSet`)

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/orders/` | List authenticated user's orders (Paginated) | Yes (`Token`) |
| `POST` | `/api/orders/` | Create an order for authenticated user | Yes (`Token`) |
| `GET` | `/api/orders/<id>/` | Retrieve user's specific order | Yes (`Token`) |
| `PUT` | `/api/orders/<id>/` | Full update user's specific order | Yes (`Token`) |
| `PATCH` | `/api/orders/<id>/` | Partial update user's specific order | Yes (`Token`) |
| `DELETE` | `/api/orders/<id>/` | Delete user's specific order | Yes (`Token`) |

---

## Sample Requests & Responses

### 1. Obtaining an Auth Token

**Request**: `POST /api/token/`
```json
{
    "username": "john_doe",
    "password": "securepassword123"
}
```

**Response**: `200 OK`
```json
{
    "token": "e3a89e634704b1239f82d456789abcde12345678"
}
```

### 2. Category Resource

**POST `/api/categories/` Request**:
```json
{
    "name": "Pizza",
    "description": "Freshly baked pizzas with standard and gourmet toppings"
}
```

**Response**: `201 Created`
```json
{
    "id": 1,
    "name": "Pizza",
    "description": "Freshly baked pizzas with standard and gourmet toppings"
}
```

### 3. MenuItem Resource

**POST `/api/menu-items/` Request**:
```json
{
    "name": "Margherita Pizza",
    "price": "12.99",
    "category": 1,
    "is_available": true
}
```

**Response**: `201 Created`
```json
{
    "id": 1,
    "name": "Margherita Pizza",
    "price": "12.99",
    "category": 1,
    "is_available": true
}
```

### 4. Order Resource

**POST `/api/orders/` Request** *(Header: `Authorization: Token e3a89e634704b1239f82d456789abcde12345678`)*:
```json
{
    "item": 1,
    "quantity": 2,
    "status": "pending"
}
```

**Response**: `201 Created`
```json
{
    "id": 1,
    "user": 2,
    "item": 1,
    "quantity": 2,
    "status": "pending",
    "created_at": "2026-08-18T21:55:00.000000Z"
}
```

---

## Validation Rules & Examples

### 1. Category Name Validation
- **Rule**: `name` cannot be empty or whitespace-only.
- **Request**: `POST /api/categories/`
  ```json
  {
      "name": "   ",
      "description": "Test"
  }
  ```
- **Response**: `400 Bad Request`
  ```json
  {
      "name": [
          "Category name cannot be empty."
      ]
  }
  ```

### 2. MenuItem Price Validation
- **Rule**: `price` must be greater than 0 (`price > 0`).
- **Request**: `POST /api/menu-items/`
  ```json
  {
      "name": "Free Soda",
      "price": "0.00",
      "category": 1
  }
  ```
- **Response**: `400 Bad Request`
  ```json
  {
      "price": [
          "Price must be greater than 0."
      ]
  }
  ```

### 3. Order Quantity Validation
- **Rule**: `quantity` must be at least 1 (`quantity >= 1`).
- **Request**: `POST /api/orders/`
  ```json
  {
      "item": 1,
      "quantity": 0
  }
  ```
- **Response**: `400 Bad Request`
  ```json
  {
      "quantity": [
          "Quantity must be at least 1."
      ]
  }
  ```

### 4. Unauthorized Order Request
- **Rule**: Accessing `/api/orders/` without token header returns `401 Unauthorized`.
- **Response**: `401 Unauthorized`
  ```json
  {
      "detail": "Authentication credentials were not provided."
  }
  ```

---

## Pagination Example

`OrderViewSet` list endpoint uses `PageNumberPagination` configured to **5 items per page** (`PAGE_SIZE = 5`).

**Request**: `GET /api/orders/`

**Response**: `200 OK`
```json
{
    "count": 7,
    "next": "http://127.0.0.1:8000/api/orders/?page=2",
    "previous": null,
    "results": [
        {
            "id": 7,
            "user": 2,
            "item": 1,
            "quantity": 1,
            "status": "pending",
            "created_at": "2026-08-18T21:55:00.000000Z"
        },
        {
            "id": 6,
            "user": 2,
            "item": 2,
            "quantity": 2,
            "status": "confirmed",
            "created_at": "2026-08-18T21:54:00.000000Z"
        },
        {
            "id": 5,
            "user": 2,
            "item": 1,
            "quantity": 1,
            "status": "pending",
            "created_at": "2026-08-18T21:53:00.000000Z"
        },
        {
            "id": 4,
            "user": 2,
            "item": 1,
            "quantity": 3,
            "status": "delivered",
            "created_at": "2026-08-18T21:52:00.000000Z"
        },
        {
            "id": 3,
            "user": 2,
            "item": 2,
            "quantity": 1,
            "status": "pending",
            "created_at": "2026-08-18T21:51:00.000000Z"
        }
    ]
}
```

---

## Status Filtering Example

Filter user orders by status (`pending`, `confirmed`, `delivered`) using the `?status=` query parameter.

**Request**: `GET /api/orders/?status=confirmed`

**Response**: `200 OK`
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 6,
            "user": 2,
            "item": 2,
            "quantity": 2,
            "status": "confirmed",
            "created_at": "2026-08-18T21:54:00.000000Z"
        }
    ]
}
```

---

## Sample Test Data

Use the following test data when testing via Postman or Django Admin:

### Categories
1. **Name**: `Pizza` | **Description**: `Delicious hand-tossed pizzas`
2. **Name**: `Burger` | **Description**: `Gourmet beef and veggie burgers`
3. **Name**: `Beverages` | **Description**: `Cold beverages and soft drinks`

### Menu Items
1. **Name**: `Margherita Pizza` | **Price**: `12.99` | **Category**: `Pizza` (ID: 1)
2. **Name**: `Cheese Burger` | **Price**: `8.99` | **Category**: `Burger` (ID: 2)
3. **Name**: `Cold Coffee` | **Price**: `4.50` | **Category**: `Beverages` (ID: 3)

### Orders
1. **Item**: `1` | **Quantity**: `2` | **Status**: `pending`
2. **Item**: `2` | **Quantity**: `1` | **Status**: `confirmed`
3. **Item**: `3` | **Quantity**: `3` | **Status**: `delivered`

---

## Running Unit Tests

Run the full automated test suite containing 10 comprehensive API test cases:

```bash
python manage.py test
```

**Test Coverage Includes:**
1. Category listing and creation
2. MenuItem creation
3. MenuItem invalid price validation (0 and negative prices)
4. Order creation with token authentication
5. Order listing (user isolation)
6. Order pagination (5 items per page)
7. Order status filtering (`?status=pending`, etc.)
8. Unauthorized order request (HTTP 401)
9. Object-level security (cannot access another user's order ID -> HTTP 404)
10. Order quantity validation (quantity < 1 -> HTTP 400)

---

## Postman Testing Screenshots

Below are the labeled screenshot placeholders documenting API execution in Postman:

### 1. Category GET
![Category GET Placeholder](docs/screenshots/01_category_get.png)
*Description: Listing categories via GET `/api/categories/` returning HTTP 200 OK.*

### 2. Category POST
![Category POST Placeholder](docs/screenshots/02_category_post.png)
*Description: Creating a new category via POST `/api/categories/` returning HTTP 201 Created.*

### 3. MenuItem POST
![MenuItem POST Placeholder](docs/screenshots/03_menu_item_post.png)
*Description: Creating a menu item via POST `/api/menu-items/` returning HTTP 201 Created.*

### 4. MenuItem GET
![MenuItem GET Placeholder](docs/screenshots/04_menu_item_get.png)
*Description: Listing menu items via GET `/api/menu-items/` returning HTTP 200 OK.*

### 5. MenuItem Invalid Price Validation
![MenuItem Invalid Price Placeholder](docs/screenshots/05_menu_item_invalid_price.png)
*Description: Attempting to create menu item with price `0.00` returning HTTP 400 Bad Request with validation error message.*

### 6. Order POST with Token
![Order POST Placeholder](docs/screenshots/06_order_post_token.png)
*Description: Creating an order with `Authorization: Token <token>` header returning HTTP 201 Created and automatically setting user.*

### 7. Order GET with Token
![Order GET Placeholder](docs/screenshots/07_order_get_token.png)
*Description: Fetching authenticated user's orders via GET `/api/orders/` returning HTTP 200 OK.*

### 8. Order Pagination
![Order Pagination Placeholder](docs/screenshots/08_order_pagination.png)
*Description: Paginated order response demonstrating `count`, `next`, `previous`, and 5 items in `results` array.*

### 9. Order Status Filtering
![Order Status Filtering Placeholder](docs/screenshots/09_order_status_filtering.png)
*Description: Filtering orders by status via GET `/api/orders/?status=pending` returning filtered results.*

### 10. Unauthorized Order Request (HTTP 401)
![Unauthorized Order Request Placeholder](docs/screenshots/10_order_unauthorized.png)
*Description: Accessing GET `/api/orders/` without authentication header returning HTTP 401 Unauthorized.*
