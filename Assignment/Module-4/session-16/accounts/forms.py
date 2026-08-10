from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
    mobile_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '••••••••'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '••••••••'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
            
        return cleaned_data

class OTPRequestForm(forms.Form):
    mobile_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control bg-dark text-light border-secondary',
        'placeholder': 'Enter mobile number with country code (e.g. +1234567890)'
    }))

class OTPVerifyForm(forms.Form):
    otp_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={
        'class': 'form-control bg-dark text-light border-secondary',
        'placeholder': 'Enter 6-digit OTP'
    }))
