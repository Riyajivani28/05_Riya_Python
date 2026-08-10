from django.core.management.base import BaseCommand
from locations.models import Cafe, PickupPoint


class Command(BaseCommand):
    help = "Seeds sample Cafe and PickupPoint records for testing GeoLocate Hub features."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Clearing existing sample records..."))
        Cafe.objects.all().delete()
        PickupPoint.objects.all().delete()

        cafes_data = [
            # Ahmedabad Cafes
            {
                "name": "Zen Cafe",
                "address": "Amdavad Ni Gufa, Near Gujarat University, Ahmedabad",
                "latitude": 23.0370,
                "longitude": 72.5510,
                "city": "Ahmedabad"
            },
            {
                "name": "Mocha Cafe & Bar",
                "address": "CG Road, Navrangpura, Ahmedabad",
                "latitude": 23.0305,
                "longitude": 72.5576,
                "city": "Ahmedabad"
            },
            {
                "name": "The Dark Cafe",
                "address": "University Road, Opp. LD Engineering, Ahmedabad",
                "latitude": 23.0330,
                "longitude": 72.5490,
                "city": "Ahmedabad"
            },
            {
                "name": "Crafto Bistro & Cafe",
                "address": "Vastrapur Lake Front, Ahmedabad",
                "latitude": 23.0350,
                "longitude": 72.5290,
                "city": "Ahmedabad"
            },
            {
                "name": "Roastea Cultur Cafe",
                "address": "Satellite Road, Near ISRO, Ahmedabad",
                "latitude": 23.0280,
                "longitude": 72.5200,
                "city": "Ahmedabad"
            },
            {
                "name": "Cafe De Italiano",
                "address": "Sindhu Bhavan Road, Bodakdev, Ahmedabad",
                "latitude": 23.0450,
                "longitude": 72.5080,
                "city": "Ahmedabad"
            },
            {
                "name": "Starbucks Coffee",
                "address": "Prahlad Nagar Corporate Road, Ahmedabad",
                "latitude": 23.0120,
                "longitude": 72.5050,
                "city": "Ahmedabad"
            },
            # Rajkot Cafes
            {
                "name": "Cafe Coffee Day",
                "address": "Kalawad Road, Opp. KKV Hall, Rajkot",
                "latitude": 22.2850,
                "longitude": 70.7750,
                "city": "Rajkot"
            },
            {
                "name": "The Coffee Factory",
                "address": "Yagnik Road, Near Imperial Palace, Rajkot",
                "latitude": 22.2960,
                "longitude": 70.7950,
                "city": "Rajkot"
            },
            {
                "name": "Tea Post - Desi Cafe",
                "address": "150 Feet Ring Road, Near Raiya Circle, Rajkot",
                "latitude": 22.2780,
                "longitude": 70.7710,
                "city": "Rajkot"
            },
            {
                "name": "Real Paprika Cafe",
                "address": "Amin Marg, Near Crystal Mall, Rajkot",
                "latitude": 22.2900,
                "longitude": 70.7840,
                "city": "Rajkot"
            },
            {
                "name": "Chai Sutta Bar",
                "address": "University Road, Near Saurashtra University, Rajkot",
                "latitude": 22.2880,
                "longitude": 70.7680,
                "city": "Rajkot"
            }
        ]

        pickup_data = [
            # Ahmedabad Pickup Points
            {
                "name": "Blue Dart Parcel Pickup Hub",
                "address": "Ashram Road, Opp. Income Tax, Ahmedabad",
                "latitude": 23.0320,
                "longitude": 72.5700,
                "city": "Ahmedabad"
            },
            {
                "name": "DTDC Express Courier Center",
                "address": "CG Road, Navrangpura, Ahmedabad",
                "latitude": 23.0270,
                "longitude": 72.5550,
                "city": "Ahmedabad"
            },
            {
                "name": "Amazon Easy Pickup Locker",
                "address": "Vastrapur Lake Commercial Complex, Ahmedabad",
                "latitude": 23.0360,
                "longitude": 72.5260,
                "city": "Ahmedabad"
            },
            {
                "name": "Delhivery Smart Pickup Station",
                "address": "Satellite Road, Near Star Bazaar, Ahmedabad",
                "latitude": 23.0220,
                "longitude": 72.5180,
                "city": "Ahmedabad"
            },
            # Rajkot Pickup Points
            {
                "name": "Flipkart Express Pickup Point",
                "address": "Yagnik Road, Near Jilla Panchayat, Rajkot",
                "latitude": 22.2950,
                "longitude": 70.7930,
                "city": "Rajkot"
            },
            {
                "name": "Amazon Locker Pickup Station",
                "address": "Kalawad Road, Near KKV Hall, Rajkot",
                "latitude": 22.2830,
                "longitude": 70.7720,
                "city": "Rajkot"
            },
            {
                "name": "DHL Express Worldwide Drop Station",
                "address": "150 Feet Ring Road, Rajkot",
                "latitude": 22.2760,
                "longitude": 70.7700,
                "city": "Rajkot"
            },
            {
                "name": "Blue Dart Courier Drop Point",
                "address": "Amin Marg, Near Women's College, Rajkot",
                "latitude": 22.2890,
                "longitude": 70.7830,
                "city": "Rajkot"
            }
        ]

        for cafe_item in cafes_data:
            Cafe.objects.create(**cafe_item)

        for pickup_item in pickup_data:
            PickupPoint.objects.create(**pickup_item)

        self.stdout.write(self.style.SUCCESS(
            f"Successfully seeded {len(cafes_data)} Cafes and {len(pickup_data)} Pickup Points into SQLite database!"
        ))
