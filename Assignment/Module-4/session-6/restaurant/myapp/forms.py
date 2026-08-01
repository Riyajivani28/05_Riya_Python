from django import forms

class AddRestaurantForm(forms.Form):

    restaurant_name = forms.CharField(
        min_length=3,
        label="Restaurant Name"
    )

    cuisine_type = forms.CharField(
        label="Cuisine Type"
    )

    contact_email = forms.EmailField(
        label="Contact Email"
    )