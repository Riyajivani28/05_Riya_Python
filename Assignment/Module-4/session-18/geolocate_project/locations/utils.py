import math
import requests
from django.conf import settings

# Pre-defined fallback coordinates for common assignment & demonstration locations
DEMO_LOCATIONS = {
    "iim ahmedabad": {
        "formatted_address": "Indian Institute of Management Ahmedabad, Vastrapur, Ahmedabad, Gujarat 380015",
        "lat": 23.0338,
        "lng": 72.5467
    },
    "iim ahmedabad, gujarat": {
        "formatted_address": "Indian Institute of Management Ahmedabad, Vastrapur, Ahmedabad, Gujarat 380015",
        "lat": 23.0338,
        "lng": 72.5467
    },
    "rajkot": {
        "formatted_address": "Rajkot, Gujarat, India",
        "lat": 22.3039,
        "lng": 70.8022
    },
    "rajkot, gujarat": {
        "formatted_address": "Rajkot, Gujarat, India",
        "lat": 22.3039,
        "lng": 70.8022
    },
    "la pino's pizza": {
        "formatted_address": "La Pino's Pizza, Kalawad Road, Rajkot, Gujarat",
        "lat": 22.2855,
        "lng": 70.7760
    },
    "la pino's pizza, rajkot": {
        "formatted_address": "La Pino's Pizza, Kalawad Road, Rajkot, Gujarat",
        "lat": 22.2855,
        "lng": 70.7760
    },
    "taj mahal": {
        "formatted_address": "Taj Mahal, Dharmapuri, Tajganj, Agra, Uttar Pradesh 282001",
        "lat": 27.1751,
        "lng": 78.0421
    },
    "taj mahal, agra": {
        "formatted_address": "Taj Mahal, Dharmapuri, Tajganj, Agra, Uttar Pradesh 282001",
        "lat": 27.1751,
        "lng": 78.0421
    },
    "ashram road, ahmedabad": {
        "formatted_address": "Ashram Road, Navrangpura, Ahmedabad, Gujarat 380009",
        "lat": 23.0320,
        "lng": 72.5700
    },
    "satellite, ahmedabad": {
        "formatted_address": "Satellite, Ahmedabad, Gujarat 380015",
        "lat": 23.0280,
        "lng": 72.5200
    },
    "kalawad road, rajkot": {
        "formatted_address": "Kalawad Road, Rajkot, Gujarat 360005",
        "lat": 22.2830,
        "lng": 70.7720
    },
    "yagnik road, rajkot": {
        "formatted_address": "Yagnik Road, Rajkot, Gujarat 360001",
        "lat": 22.2950,
        "lng": 70.7930
    },
    "ahmedabad": {
        "formatted_address": "Ahmedabad, Gujarat, India",
        "lat": 23.0225,
        "lng": 72.5714
    },
    "mumbai": {
        "formatted_address": "Mumbai, Maharashtra, India",
        "lat": 19.0760,
        "lng": 72.8777
    }
}


def geocode_address(address):
    """
    Geocodes an address string using the Google Geocoding API via HTTP `requests`.
    
    If Google Maps API key is missing, default, or unconfigured, it gracefully falls back to:
    1. Pre-configured demo coordinates dictionary for instant local lookup.
    2. Free OpenStreetMap Nominatim geocoding API.
    
    This ensures the application never crashes even without an active paid Google API Key.
    """
    if not address or not str(address).strip():
        return {"error": "Please enter an address."}

    clean_address = str(address).strip()
    api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

    # Try Google Geocoding API if a non-placeholder API key is set
    if api_key and api_key not in ['your_google_maps_api_key', 'your_google_maps_api_key_here']:
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            'address': clean_address,
            'key': api_key
        }

        try:
            response = requests.get(url, params=params, timeout=8)
            if response.status_code == 200:
                data = response.json()
                status = data.get('status')

                if status == 'OK' and data.get('results'):
                    first_result = data['results'][0]
                    location = first_result['geometry']['location']
                    return {
                        "formatted_address": first_result.get('formatted_address', clean_address),
                        "lat": float(location['lat']),
                        "lng": float(location['lng'])
                    }
                elif status == 'ZERO_RESULTS':
                    return {"error": "No location found for this address. Please try a different address."}
        except requests.exceptions.RequestException:
            pass  # Proceed to smart fallback

    # Smart Fallback 1: Local Demo Dictionary for Instant Geocoding
    lower_query = clean_address.lower()
    for loc_key, coords in DEMO_LOCATIONS.items():
        if loc_key in lower_query or lower_query in loc_key:
            return {
                "formatted_address": coords["formatted_address"],
                "lat": coords["lat"],
                "lng": coords["lng"]
            }

    # Smart Fallback 2: Free OpenStreetMap Nominatim Geocoding API
    try:
        osm_url = "https://nominatim.openstreetmap.org/search"
        headers = {'User-Agent': 'GeoLocateHub/1.0 (contact@geolocatehub.app)'}
        osm_params = {'q': clean_address, 'format': 'json', 'limit': 1}
        osm_resp = requests.get(osm_url, params=osm_params, headers=headers, timeout=6)
        
        if osm_resp.status_code == 200:
            osm_data = osm_resp.json()
            if osm_data and len(osm_data) > 0:
                res = osm_data[0]
                return {
                    "formatted_address": res.get('display_name', clean_address),
                    "lat": float(res['lat']),
                    "lng": float(res['lon'])
                }
    except Exception:
        pass

    return {
        "error": f"No location found for '{clean_address}'. Please add your GOOGLE_MAPS_API_KEY in .env file or try searching 'IIM Ahmedabad, Gujarat' or 'Rajkot, Gujarat'."
    }


def calculate_distance(lat1, lng1, lat2, lng2):
    """
    Manually calculates the great-circle distance between two geographical points 
    using the Haversine formula.

    R = 6371 (Earth radius in km)
    dlat = radians(lat2 - lat1)
    dlon = radians(lng2 - lng1)
    a = sin²(dlat/2) + cos(lat1) * cos(lat2) * sin²(dlon/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    No external libraries (geopy, haversine) are used.
    """
    R = 6371.0  # Earth's radius in kilometers

    # Convert latitude and longitude from degrees to radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lng2 - lng1)

    # Haversine formula
    a = (math.sin(dlat / 2.0) ** 2) + math.cos(phi1) * math.cos(phi2) * (math.sin(dlon / 2.0) ** 2)
    
    # Clamp 'a' between 0.0 and 1.0 to prevent floating point inaccuracies
    a = max(0.0, min(1.0, a))
    
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

    distance = R * c
    return round(distance, 2)


def find_nearby_cafes(user_lat, user_lng, cafes, max_distance=3.0):
    """
    Filters cafe records to find those within `max_distance` (default 3.0 km) 
    using the manual Haversine formula, and returns them sorted by distance (nearest first).
    """
    nearby_cafes = []

    for cafe in cafes:
        c_lat = cafe.latitude if hasattr(cafe, 'latitude') else cafe.get('lat', cafe.get('latitude'))
        c_lng = cafe.longitude if hasattr(cafe, 'longitude') else cafe.get('lng', cafe.get('longitude'))
        c_name = cafe.name if hasattr(cafe, 'name') else cafe.get('name')
        c_address = cafe.address if hasattr(cafe, 'address') else cafe.get('address')
        c_city = getattr(cafe, 'city', '') if hasattr(cafe, 'city') else cafe.get('city', '')

        if c_lat is None or c_lng is None:
            continue

        distance = calculate_distance(user_lat, user_lng, float(c_lat), float(c_lng))

        if distance <= max_distance:
            nearby_cafes.append({
                "id": getattr(cafe, 'id', None),
                "name": c_name,
                "address": c_address,
                "city": c_city,
                "lat": float(c_lat),
                "lng": float(c_lng),
                "distance": distance
            })

    nearby_cafes.sort(key=lambda item: item['distance'])
    return nearby_cafes
