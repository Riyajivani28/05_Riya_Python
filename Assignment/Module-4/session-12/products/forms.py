from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Wireless Headphones'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 1999.00', 'step': '0.01'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Electronics'}),
        }
        labels = {
            'name': 'Product Name',
            'price': 'Price (₹)',
            'category': 'Category',
        }
