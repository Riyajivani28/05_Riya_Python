from django import forms

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'name@example.com',
            'class': 'form-input',
            'required': True,
            'id': 'id_email'
        })
    )

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(
        label="Enter OTP",
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'placeholder': '123456',
            'class': 'form-input otp-input',
            'required': True,
            'id': 'id_otp',
            'pattern': '[0-9]{6}',
            'maxlength': '6'
        })
    )
    def clean_otp(self):
        otp = self.cleaned_data.get('otp', '').strip()
        if not otp.isdigit() or len(otp) != 6:
            raise forms.ValidationError("OTP must be a 6-digit number.")
        return otp
