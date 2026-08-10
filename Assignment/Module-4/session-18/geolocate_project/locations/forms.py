from django import forms


class LiveMapSearchForm(forms.Form):
    address = forms.CharField(
        label="Enter Any Address, Restaurant, City, or Location",
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'e.g. Taj Mahal, Agra or IIM Ahmedabad or Rajkot, Gujarat',
            'autocomplete': 'off',
            'id': 'live_map_search_input'
        })
    )


class GeocodeForm(forms.Form):
    address = forms.CharField(
        label="Enter Location / Address",
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'e.g. IIM Ahmedabad, Gujarat',
            'autocomplete': 'off',
            'id': 'geocode_address_input'
        })
    )


class RestaurantForm(forms.Form):
    name = forms.CharField(
        label="Restaurant Name",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "e.g. La Pino's Pizza",
            'autocomplete': 'off',
            'id': 'restaurant_name_input'
        })
    )
    address = forms.CharField(
        label="Restaurant Address",
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. Rajkot, Gujarat',
            'autocomplete': 'off',
            'id': 'restaurant_address_input'
        })
    )


class NearbyCafeForm(forms.Form):
    address = forms.CharField(
        label="Your Current Address / Location",
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'e.g. Rajkot, Gujarat or IIM Ahmedabad, Gujarat',
            'autocomplete': 'off',
            'id': 'cafe_address_input'
        })
    )


class PickupSearchForm(forms.Form):
    address = forms.CharField(
        label="Enter Your Current Address",
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'e.g. Rajkot, Gujarat or Satellite, Ahmedabad',
            'autocomplete': 'off',
            'id': 'pickup_address_input'
        })
    )
