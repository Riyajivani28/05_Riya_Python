from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine', 'rating']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter restaurant name'
            }),
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'step': 0.1
            }),
        }

    # Validate name
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name.strip()) < 3:
            raise forms.ValidationError(
                "Restaurant name must be at least 3 characters long."
            )

        return name

    # Validate rating
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')

        if rating < 1 or rating > 5:
            raise forms.ValidationError(
                "Rating must be between 1 and 5."
            )

        return rating