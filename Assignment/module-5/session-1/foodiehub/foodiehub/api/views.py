from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# =====================================================================
# Comparison between JSON and XML
# =====================================================================
"""
JSON vs XML Comparison:
- JSON (JavaScript Object Notation) is lightweight, easy to read, faster to parse, and directly maps to native data structures like objects/dictionaries.
- XML (Extensible Markup Language) is verbose, uses opening and closing tags, and requires a dedicated parser, but supports rich schema validation and attributes.

Sample response representing a Flipkart product (Name: Wireless Headphones, Price: 1999):

JSON Format:
{
    "product": {
        "name": "Wireless Headphones",
        "price": 1999
    }
}

XML Format:
<product>
    <name>Wireless Headphones</name>
    <price>1999</price>
</product>
"""

# Create your views here.

@api_view(['GET'])
def hello_spotify(request):
    return Response({
        "message": "Hello, Spotify Fans!"
    })

