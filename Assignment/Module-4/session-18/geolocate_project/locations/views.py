from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from .forms import LiveMapSearchForm, GeocodeForm, RestaurantForm, NearbyCafeForm, PickupSearchForm
from .models import Cafe, PickupPoint
from .utils import geocode_address, calculate_distance, find_nearby_cafes


def home_view(request):
    """
    Renders the GeoLocate Hub modern homepage.
    """
    context = {
        'title': 'GeoLocate Hub - Smart Location Services',
    }
    return render(request, 'home.html', context)


def live_map_search_view(request):
    """
    Live Google Maps Search View (/live-map/).
    Geocodes any location, restaurant, city, or landmark, centers live map on coordinates,
    and displays marker + detailed address info below.
    """
    form = LiveMapSearchForm(request.POST or None)
    result = None
    error_message = None
    google_maps_api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

    if request.method == 'POST':
        if form.is_valid():
            address = form.cleaned_data['address']
            geocoded = geocode_address(address)
            
            if 'error' in geocoded:
                error_message = geocoded['error']
                messages.error(request, error_message)
            else:
                result = {
                    'query': address,
                    'formatted_address': geocoded['formatted_address'],
                    'lat': geocoded['lat'],
                    'lng': geocoded['lng']
                }
                messages.success(request, f"Successfully mapped '{address}'.")
        else:
            messages.error(request, "Please enter a valid address or location to search.")

    context = {
        'title': 'Live Map Search',
        'form': form,
        'result': result,
        'error_message': error_message,
        'google_maps_api_key': google_maps_api_key
    }
    return render(request, 'live_map.html', context)


def geocode_view(request):
    """
    Address Geocoder View (/geocode/).
    Converts an address input into latitude & longitude via Google Geocoding API.
    """
    form = GeocodeForm(request.POST or None)
    result = None
    error_message = None
    google_maps_api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

    if request.method == 'POST':
        if form.is_valid():
            address = form.cleaned_data['address']
            geocoded = geocode_address(address)
            
            if 'error' in geocoded:
                error_message = geocoded['error']
                messages.error(request, error_message)
            else:
                result = {
                    'searched_address': address,
                    'query': address,
                    'formatted_address': geocoded['formatted_address'],
                    'lat': geocoded['lat'],
                    'lng': geocoded['lng']
                }
                messages.success(request, f"Successfully geocoded address for '{address}'.")
        else:
            messages.error(request, "Please enter a valid address.")

    context = {
        'title': 'Address Geocoder',
        'form': form,
        'result': result,
        'error_message': error_message,
        'google_maps_api_key': google_maps_api_key
    }
    return render(request, 'geocode.html', context)


def show_restaurant_location(request):
    """
    Restaurant Location View (/restaurant-location/).
    Geocodes a restaurant's address and dynamically embeds it on a Google Map.
    """
    form = RestaurantForm(request.POST or None)
    restaurant_data = None
    error_message = None
    google_maps_api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            
            geocoded = geocode_address(address)
            if 'error' in geocoded:
                error_message = geocoded['error']
                messages.error(request, error_message)
            else:
                restaurant_data = {
                    'name': name,
                    'address': address,
                    'formatted_address': geocoded['formatted_address'],
                    'lat': geocoded['lat'],
                    'lng': geocoded['lng']
                }
                messages.success(request, f"Found location for '{name}'.")
        else:
            messages.error(request, "Please fill out all form fields correctly.")

    context = {
        'title': 'Restaurant Map View',
        'form': form,
        'restaurant': restaurant_data,
        'error_message': error_message,
        'google_maps_api_key': google_maps_api_key
    }
    return render(request, 'restaurant_location.html', context)


def nearby_cafes_view(request):
    """
    Nearby Cafes View (/nearby-cafes/).
    Geocodes user address and uses the manual Haversine formula to find cafes within 3 km.
    """
    form = NearbyCafeForm(request.POST or None)
    results = None
    user_location = None
    error_message = None
    google_maps_api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

    if request.method == 'POST':
        if form.is_valid():
            user_address = form.cleaned_data['address']
            geocoded = geocode_address(user_address)
            
            if 'error' in geocoded:
                error_message = geocoded['error']
                messages.error(request, error_message)
            else:
                u_lat = geocoded['lat']
                u_lng = geocoded['lng']
                user_location = {
                    'address': user_address,
                    'formatted_address': geocoded['formatted_address'],
                    'lat': u_lat,
                    'lng': u_lng
                }

                # Query cafes from database
                all_cafes = list(Cafe.objects.all())
                
                if not all_cafes:
                    messages.warning(request, "No cafe records found in the database. Please run sample data seed command.")
                    results = []
                else:
                    # Calculate distance using manual Haversine formula
                    results = find_nearby_cafes(u_lat, u_lng, all_cafes, max_distance=3.0)
                    
                    if not results:
                        messages.warning(request, "No cafes were found within 3 km of your location.")
                    else:
                        messages.success(request, f"Found {len(results)} cafe(s) within 3 km.")
        else:
            messages.error(request, "Please enter a valid address.")

    context = {
        'title': 'Nearby Cafes Search',
        'form': form,
        'user_location': user_location,
        'cafes': results,
        'error_message': error_message,
        'google_maps_api_key': google_maps_api_key
    }
    return render(request, 'nearby_cafes.html', context)


def search_by_distance(request):
    """
    Pickup Point Search View (/pickup-points/).
    Geocodes user address, queries database for pickup points, 
    calculates distance via manual Haversine formula, and displays sorted results (nearest first).
    """
    form = PickupSearchForm(request.POST or None)
    google_maps_api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY', '')

    if request.method == 'POST' and form.is_valid():
        user_address = form.cleaned_data['address']
        geocoded = geocode_address(user_address)

        if 'error' in geocoded:
            messages.error(request, geocoded['error'])
            context = {
                'title': 'Pickup Point Finder',
                'form': form,
                'error_message': geocoded['error'],
                'google_maps_api_key': google_maps_api_key
            }
            return render(request, 'pickup_search.html', context)

        u_lat = geocoded['lat']
        u_lng = geocoded['lng']
        user_location = {
            'address': user_address,
            'formatted_address': geocoded['formatted_address'],
            'lat': u_lat,
            'lng': u_lng
        }

        # Query all pickup points from database
        pickup_queryset = PickupPoint.objects.all()

        if not pickup_queryset.exists():
            messages.warning(request, "No pickup points found in the system.")
            context = {
                'title': 'Pickup Search Results',
                'form': form,
                'user_location': user_location,
                'pickup_points': [],
                'google_maps_api_key': google_maps_api_key
            }
            return render(request, 'pickup_results.html', context)

        # Calculate manual Haversine distance for each point
        calculated_points = []
        for pt in pickup_queryset:
            dist = calculate_distance(u_lat, u_lng, pt.latitude, pt.longitude)
            calculated_points.append({
                'id': pt.id,
                'name': pt.name,
                'address': pt.address,
                'city': pt.city,
                'lat': pt.latitude,
                'lng': pt.longitude,
                'distance': dist,
                'is_nearest': False
            })

        # Sort nearest -> farthest
        calculated_points.sort(key=lambda item: item['distance'])

        if calculated_points:
            calculated_points[0]['is_nearest'] = True

        messages.success(request, f"Located {len(calculated_points)} pickup point(s) sorted by distance.")

        context = {
            'title': 'Pickup Search Results',
            'form': form,
            'user_location': user_location,
            'pickup_points': calculated_points,
            'nearest_point': calculated_points[0] if calculated_points else None,
            'google_maps_api_key': google_maps_api_key
        }
        return render(request, 'pickup_results.html', context)

    # GET request
    context = {
        'title': 'Pickup Point Finder',
        'form': form,
        'google_maps_api_key': google_maps_api_key
    }
    return render(request, 'pickup_search.html', context)
