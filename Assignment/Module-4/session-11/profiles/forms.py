from django import forms
from .models import InfluencerProfile

class InfluencerProfileForm(forms.ModelForm):
    class Meta:
        model = InfluencerProfile
        fields = ['display_name', 'bio', 'phone_number', 'profile_pic']
        widgets = {
            'display_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Display Name'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your bio...'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit Phone Number'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            phone_number = phone_number.strip()
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise forms.ValidationError('Phone number must be exactly 10 digits.')
        return phone_number
