from django import forms 
from .models import PasswordSafe

class AddpasswordForm(forms.ModelForm):
    class Meta:
        model = PasswordSafe
        fields = ('platform_name','email_address','password')

        widgets = {
            'platform_name': forms.Select(attrs={'class': 'w-50'}),
            'email_address': forms.EmailInput(attrs={'class': 'w-50','placeholder':'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'w-50','placeholder':'Password'}),
        }