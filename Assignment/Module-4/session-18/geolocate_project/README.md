# GeoLocate Hub 📍

A dynamic Django web application demonstrating Google Maps Geocoding API integration, embedded interactive maps, live location search, manual **Haversine formula distance calculation**, nearby cafe finder (within 3 km), and nearest pickup-point search.

---

## 🚀 Key Features

1. **Live Google Maps Search (`/live-map/`)**:
   - Dynamic live location search for any address, restaurant, city, or landmark.
   - Geocodes search query via Google Geocoding API, centers live Google Map on coordinates, and drops a location marker with InfoWindow.
   - Displays Formatted Address, Latitude, and Longitude below the map.

2. **Address Geocoder (`/geocode/`)**:
   - Converts any human-readable location into accurate latitude and longitude coordinates with an embedded map view.
   - Comprehensive error handling for empty inputs, invalid locations, network failures, and `ZERO_RESULTS`.

3. **Restaurant Location Map (`/restaurant-location/`)**:
   - Geocodes user-submitted restaurant name and address in real-time.
   - Embeds an interactive Google Map with a dynamic marker at the geocoded coordinates.

4. **Nearby Cafes Finder (`/nearby-cafes/`)**:
   - Converts user address into coordinates.
   - Manually calculates great-circle distance to all cafes in the SQLite database using the Haversine formula.
   - Filters cafes within a 3.0 km radius and sorts them from nearest to farthest.
   - Interactive Google Map featuring a blue pin for user location and red pins with InfoWindows for cafe markers.

5. **Pickup Point Search (`/pickup-points/`)**:
   - Finds package pickup points nearest to the user's address.
   - Calculates manual Haversine distance for all database records and ranks them nearest to farthest.
   - Highlights the top **Nearest Pickup Point** with a badge.
   - Dynamic map displaying user location and all pickup point markers.

6. **Pure Math Haversine Distance**:
   - Implemented manually using Python's native `math` module without any third-party distance/geolocation libraries (`geopy`, `haversine`).

7. **Django Admin CRUD (`/admin/`)**:
   - Complete admin management interface for `Cafe` and `PickupPoint` models.

---

## 🛠️ Technology Stack

- **Backend**: Django 5.x, Python 3.11+, SQLite
- **API Integration**: Google Geocoding API & Google Maps JavaScript API via `requests`
- **Environment Management**: `python-dotenv`
- **Frontend**: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript

---

## 📂 Project Structure

```text
geolocate_project/
│
├── manage.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
│
├── geolocate_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── locations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── forms.py
│   ├── utils.py
│   └── management/
│       └── commands/
│           └── seed_data.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── live_map.html
│   ├── geocode.html
│   ├── restaurant_location.html
│   ├── nearby_cafes.html
│   ├── pickup_search.html
│   └── pickup_results.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

---

## 🔑 Google Maps API Setup Instructions

To obtain and configure your Google Maps API key:

1. **Go to Google Cloud Console**:
   Visit [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a Project**:
   Click on the project dropdown at the top and click **New Project**. Name it `GeoLocate-Hub`.

3. **Enable Required APIs**:
   Search and **Enable** the following APIs:
   - **Geocoding API** (For address → latitude/longitude conversion)
   - **Maps JavaScript API** (For displaying interactive web maps)

4. **Create API Key**:
   Go to **APIs & Services** > **Credentials**.
   Click **+ CREATE CREDENTIALS** > **API Key**. Copy your generated key.

5. **Configure Environment File**:
   Create a `.env` file in the project root directory:
   ```env
   GOOGLE_MAPS_API_KEY=your_actual_google_maps_api_key_here
   SECRET_KEY=django-insecure-geolocate-hub-key-2026
   DEBUG=True
   ```

---

## ⚙️ Installation & Running the Application

### 1. Navigate to Project Directory
```bash
cd geolocate_project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations & Seed Data
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
```

### 4. Run Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🌐 Application Routes

- `/` — Homepage
- `/live-map/` — Live Google Maps Search Feature
- `/geocode/` — Address Geocoder
- `/restaurant-location/` — Restaurant Location Map
- `/nearby-cafes/` — Nearby Cafes Search (&le; 3 km filter)
- `/pickup-points/` — Nearest Pickup Point Search
- `/admin/` — Django Admin Panel
